from django.contrib import admin
from django.urls import path, include
from rest_framework.authtoken import views
from rest_framework.urlpatterns import format_suffix_patterns
from .views import home
from .comment.views import CommentList
from .comment.views import CommentDetail
from .faculty.views import FacultyList
from .faculty.views import FacultyDetail
from .user.views import UserList
from .user.views import UserDetail
from .role.views import RoleList
from .role.views import RoleDetail
from .contribution.views import ContributionList
from .contribution.views import ContributionDetail
from .info.views import InfoList
from .info.views import InfoDetail


urlpatterns = [
    path('', home, name='api.home'),
    path('users/',UserList.as_view(),name='user-list'),
    path('users/<int:pk>/',UserDetail.as_view(),name='user-detail'),
    path('info/',InfoList.as_view(),name='info-list'),
    path('info/<int:pk>/',InfoDetail.as_view(),name='info-detail'),
    path('role/',RoleList.as_view(),name='role-list'),
    path('role/<int:pk>/',RoleDetail.as_view(),name='role-detail'),
    path('contribution/',ContributionList.as_view(),name='contribution-list'),
    path('contribution/<int:pk>/',ContributionDetail.as_view(),name='contribution-detail'),
    path('faculty/',FacultyList.as_view(),name='faculty-list'),
    path('faculty/<int:pk>/',FacultyDetail.as_view(),name='faculty-detail'),
    path('comment/',FacultyList.as_view(),name='comment-list'),
    path('comment/<int:pk>/',FacultyDetail.as_view(),name='comment-detail'),
]
