from django.db import models
from ..role.models import Role
from ..faculty.models import Faculty
# Create your models here.


class Info(models.Model):
    info_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    address = models.CharField(max_length=100)
    dob = models.DateField(auto_now=False, auto_now_add=False, blank=True)
    phone = models.CharField(max_length=11)
    email = models.EmailField(max_length=100)
    role_id = models.ForeignKey(Role, on_delete=models.CASCADE)
    faculty_id = models.ForeignKey(Faculty, on_delete=models.CASCADE, null=True)
    pass

    def __str__(self):
        return self.name
