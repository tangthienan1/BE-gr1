from django.conf.urls import url
from rest_framework import routers
from django.urls import path, include
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)
from .views import CommentList, CommentViewSet

router = routers.DefaultRouter()
router.register(r'', CommentViewSet)
urlpatterns = [
    url('^$', include(router.urls)),
    path('<int:user_id>/', CommentViewSet.as_view({'get': 'retrieve', 'post': 'update'}), name='comment-detail'),
]
