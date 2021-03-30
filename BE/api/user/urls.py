from rest_framework import routers
from django.urls import path, include

from . import views

router = routers.DefaultRouter()
router.register(r'', views.UserList)
router.register(r'UserDetail', views.UserDetail)


urlpatterns = [
    path('', include(router.urls)),
    path('', views.UserList, name='user-list'),
    path('<int:pk>/', views.UserDetail, name='user-detail'),
    path('register/', views.CustomUserCreate, name="create_user"),
]


