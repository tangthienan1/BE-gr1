from rest_framework import routers
from django.urls import path, include

from . import views

router = routers.DefaultRouter()
router.register(r'', views.InfoViewSet)



urlpatterns = [
    path('', include(router.urls)),
    path('', views.InfoViewSet, name='info-list'),
    path('<int:pk>/', views.InfoViewSet, name='info-detail'),
    path('search/', views.InfoListDetailfilter, name='info-search'),
]




