from django.db import models
from django.utils import timezone
from django.utils.translation import gettext_lazy as _
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin, BaseUserManager
from ..info.models import Info

class CustomAccountManager(BaseUserManager):

    def create_superuser(self, username, password):
        user = self.create_user(username=username, password=password)
        user.is_active = True;
        user.is_superuser = True;
        user.is_staff = True;
        user.is_admin = True;
        user.save()
        return user

    def create_user(self, username, password=None, infoID = Info):

        if not username:
            raise ValueError(_('You must provide a username'))

        user = self.model(username=username,infoID=infoID)
        user.set_password(password)
        user.save()
        return user


class User(AbstractBaseUser, PermissionsMixin):

    username = models.CharField(max_length=150, unique=True)
    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    is_superuser = models.BooleanField(default=False)
    is_admin = models.BooleanField(default=False)
    infoID = models.ForeignKey(Info, on_delete=models.CASCADE, blank=True, null=True)

    objects = CustomAccountManager()

    USERNAME_FIELD = 'username'
    # REQUIRED_FIELDS = ['username']

    def __str__(self):
        return self.username