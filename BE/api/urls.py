from django.contrib import admin
from django.urls import path, include
from rest_framework.authtoken import views
from rest_framework.urlpatterns import format_suffix_patterns
from .views import home

urlpatterns = [
    path('', home, name='api.home'),
    # path('comment/', include('api.comment.urls')),
    # path('contribution/', include('api.contribution.urls')),
    # path('faculty/', include('api.faculty.urls')),
    # path('info/', include('api.info.urls')),
    # path('role/', include('api.role.urls')),
    path('user/', include('api.user.urls')),
]
