from rest_framework import routers
from django.urls import path, include
from . import views


router = routers.DefaultRouter()
router.register(r'', viewset=views.InfoList)

urlpatterns = [
    path('', include(router.urls)),
    path('', views.InfoList, name='info-list'),
]


