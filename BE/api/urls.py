from django.contrib import admin
from django.urls import path, include
from rest_framework.authtoken import views
from rest_framework.urlpatterns import format_suffix_patterns
from .views import home

urlpatterns = [
    path('', home, name='api.home'),
    # path('users/', views.UserList.as_view(), name='user-list'),
    # path('users/<int:pk>/', views.UserDetail.as_view(), name='user-detail'),
    # path('info/', views.InfoList.as_view(), name='info-list'),
    # path('info/<int:pk>/', views.InfoDetail.as_view(), name='info-detail'),
    # path('role/', views.RoleList.as_view(), name='role-list'),
    # path('role/<int:pk>/', views.RoleDetail.as_view(), name='role-detail'),
    # path('contribution/', views.ContributionList.as_view(), name='contribution-list'),
    # path('contribution/<int:pk>/', views.ContributionDetail.as_view(), name='contribution-detail'),
    # path('faculty/', views.FacultyList.as_view(), name='faculty-list'),
    # path('faculty/<int:pk>/', views.FacultyDetail.as_view(), name='faculty-detail'),
    path('comment/', include('api.comment.urls')),
    path('contribution/', include('api.contribution.urls')),
    path('faculty/', include('api.faculty.urls')),
    path('info/', include('api.info.urls')),
    path('role/', include('api.role.urls')),
    path('user/', include('api.user.urls')),
]
