from django.db import models
from django.contrib.auth.models import AbstractUser
from ..info.models import Info


class User(AbstractUser):
    # username = models.CharField(max_length=50, unique=True, default='Anonymous')
    # password = models.CharField(max_length=100)
    # reference key to info
    info = models.OneToOneField(Info, on_delete=models.CASCADE, blank=True, null=True)

    REQUIRED_FIELDS = []
    # # session_token file t store token, default = 0 means it haven't already login
    # session_token = models.CharField(max_length=10, default=0)
