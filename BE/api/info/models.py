from django.db import models

# Create your models here.


class Info(models.Model):
    infoID = models.AutoField(primary_key=True)
    Name = models.CharField(max_length=100)
    Address = models.CharField(max_length=100)
    DoB = models.DateField(auto_now=False, auto_now_add=False, blank=True)
    Phone = models.CharField(max_length=11)
    Email = models.EmailField(max_length=100)
    roleID = models.ForeignKey('Role', on_delete=models.CASCADE,)
    facultyID = models.ForeignKey('Faculty', on_delete=models.CASCADE,)
    pass

    def __str__(self):
        return self.Name
