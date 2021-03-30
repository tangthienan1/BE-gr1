from rest_framework import routers
from django.urls import path, include

from . import views

router = routers.DefaultRouter()
router.register(r'', views.RoleViewSet)



urlpatterns = [
    path('', include(router.urls)),
    path('', views.RoleViewSet, name='role-list'),
    path('<int:pk>/', views.RoleViewSet, name='role-detail'),
]


