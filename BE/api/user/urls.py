from rest_framework import routers
from django.urls import path, include

from . import views

router = routers.DefaultRouter()
router.register(r'', views.UserViewSet)

urlpaterns = [
    path('', include(router.urls)),
    path('', views.UserViewSet, name='user-list'),
    path('<int:pk>/', views.UserViewSet, name='user-detail'),
    path('register/', views.CustomUserCreate, name="create_user"),
]


