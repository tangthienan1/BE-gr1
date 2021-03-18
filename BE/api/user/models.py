from ..info.models import Info
from django.db import models
from django.utils.translation import gettext_lazy as _
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin, BaseUserManager


class CustomAccountManager(BaseUserManager):

    def create_superuser(self, username, password):
        return self.create_user(username, password)

    def create_user(self, username, password=None):
        if not username:
            raise ValueError(_('You must provide a username'))

        user = self.model(username=username)
        user.set_password(password)
        user.save()
        return user

class User(AbstractBaseUser, PermissionsMixin):
    userID = models.AutoField(primary_key=True)
    username = models.CharField(max_length=150, unique=True)
    infoID = models.ForeignKey(Info, on_delete=models.CASCADE)

    objects = CustomAccountManager()

    USERNAME_FIELD = 'username'
    # REQUIRED_FIELDS = ['username']

    def __str__(self):
        return self.username

