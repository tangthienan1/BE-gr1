from rest_framework import routers
from django.urls import path, include

from . import views

router = routers.DefaultRouter()
router.register(r'', views.RoleList)
router.register(r'RoleDetail', views.RoleDetail)


urlpatterns = [
    path('', include(router.urls)),
    path('', views.RoleList, name='role-list'),
    path('<int:pk>/', views.RoleDetail, name='role-detail'),
]


