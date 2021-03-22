from ..info.models import Info
from django.db import models
from django.utils.translation import gettext_lazy as _
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin, BaseUserManager


class CustomAccountManager(BaseUserManager):


class User(models.Model):
    userID = models.AutoField(primary_key=True)
    userName = models.CharField(max_length=100)
    token = models.CharField(max_length=100)
    infoID = models.ForeignKey('Info', on_delete=models.CASCADE,)

    def __str__(self):
        return self.username

