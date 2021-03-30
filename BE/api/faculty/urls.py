from rest_framework import routers
from django.urls import path, include

from . import views

router = routers.DefaultRouter()
router.register(r'', views.FacultyList)
router.register(r'FacultyDetail', views.FacultyDetail)


urlpatterns = [
    path('', include(router.urls)),
    path('faculty/', views.FacultyList, name='faculty-list'),
    path('faculty/<int:pk>/', views.FacultyDetail, name='faculty-detail'),
]


