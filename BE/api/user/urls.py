from django.conf.urls import url
from rest_framework import routers
from django.urls import path, include
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)
from .views import RegisterView, LoginView, UserViewSet, LogoutView

router = routers.DefaultRouter()
router.register(r'', UserViewSet)
urlpatterns = [
    url('^$', include(router.urls)),
    path('<int:user_id>/', UserViewSet.as_view({'get': 'retrieve', 'post': 'update'}), name='user-detail'),
    path('register/', RegisterView.as_view(), name="register"),
    path('login/', LoginView.as_view(), name="login_user"),
    path('logout/', LogoutView.as_view())
]
