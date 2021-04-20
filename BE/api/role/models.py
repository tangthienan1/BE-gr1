from django.db import models

# Create your models here.


class Role(models.Model):
    role_id = models.AutoField(primary_key=True)
    role_name = models.CharField(max_length=100)
    pass

    def __str__(self):
        return self.role_name
