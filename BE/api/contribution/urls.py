from BE.api.contribution.models import Contribution
from django.urls import path
from django.urls.conf import include
from rest_framework.urlpatterns import format_suffix_patterns
from rest_framework.routers import DefaultRouter
from .views import ContributionViewSet

router = DefaultRouter()
router.register(r'contributions/', ContributionViewSet)

urlpatterns = [
    path('', include(router.urls)),
]

urlpatterns = format_suffix_patterns(urlpatterns)