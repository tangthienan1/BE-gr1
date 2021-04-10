from django.db import models


# Create your models here.


class Faculty(models.Model):
    faculty_id = models.AutoField(primary_key=True)
    faculty_name = models.CharField(max_length=100)
    pass

    def __str__(self):
        return self.facultyName
