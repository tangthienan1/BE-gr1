from django.urls import path
from django.urls.conf import include
from rest_framework.urlpatterns import format_suffix_patterns
from rest_framework.routers import DefaultRouter
from . import views

router = DefaultRouter()
router.register(r'list',views.ContributionViewSet.as_view())

urlpatterns = [
    path('', include(router.urls)),
]

urlpatterns = format_suffix_patterns(urlpatterns)