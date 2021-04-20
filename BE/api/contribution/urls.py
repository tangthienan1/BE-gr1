from django.urls import path
from django.urls.conf import include
from rest_framework.urlpatterns import format_suffix_patterns
from rest_framework.routers import DefaultRouter
from .views import ContributionViewSet

router = DefaultRouter()
router.register('', ContributionViewSet)

urlpatterns = [
    path('', include(router.urls)),
]