from rest_framework import routers
from django.urls import path, include

from . import views

router = routers.DefaultRouter()
router.register(r'', views.FacultyViewSet)



urlpatterns = [
    path('', include(router.urls)),
    path('', views.FacultyViewSet, name='faculty-list'),
    path('<int:pk>/', views.FacultyViewSet, name='faculty-detail'),
]


