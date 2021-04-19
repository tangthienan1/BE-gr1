from rest_framework.response import Response
from rest_framework import status
from rest_framework import permissions
from rest_framework import viewsets
from rest_framework.decorators import action
from .models import Contribution
from ..info.models import Info
from .serializers import ContributionSerializer
from django.core.mail import send_mail

class ContributionViewSet(viewsets.ModelViewSet):
    queryset = Contribution.objects.all()
    serializer_class = ContributionSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    
    '''
    def create(self, request, *args, **kwargs):
        serializer = ContributionSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        recipient = Info.objects.filter(faculty_id=serializer.validated_data.get('faculty_id')).filter(role_id=2)
        recipient_email = recipient.email
        send_mail(
            'New Contribution Notification',
            'A new contribution has been submitted within your faculty.\nPlease review within 14 days.',
            'no-reply@example.com',
            recipient_email, # coordinator emails here
            fail_silently=False,
        )
        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)
    '''
    def perform_create(self, serializer):
        current_info = self.request.user.info
        serializer.save(author=current_info, faculty=current_info.faculty)
        recipient = Info.objects.filter(faculty_id=serializer.validated_data.get('faculty_id')).filter(role_id=2)
        recipient_email = recipient.email
        send_mail(
            'New Contribution Notification',
            'A new contribution has been submitted within your faculty.\nPlease review within 14 days.',
            'greenwichmagazinenotiy@gmail.com',
            [recipient_email], # coordinator emails here
            fail_silently=False,
        )
    # Get list of contributions by faculty_id. Example URL : api/contribution/by-faculty/1/
    @action(detail=False, methods=['get'], url_path=r'^by-contribution/(?P<faculty_id>\d+)/$') #(?P<faculty_id>\d+)/$
    def faculty(self, request, *args, **kwargs):
        queryset = Contribution.objects.filter(faculty=self.kwargs['faculty_id'])
        serializer = ContributionSerializer(queryset, many=True)
        if not queryset:
            return Response({"detail": "Not found."}, status=status.HTTP_404_NOT_FOUND)
        return Response(serializer.data)


    # def retrieve(self, pk=None):
    #     contributions = Contribution.objects.filter(faculty_id=pk)
    
    # def get_queryset(self):
    #     queryset = self.queryset
    #     contributions = queryset.filter(faculty=self.kwargs['faculty_id'])
    #     return contributions



