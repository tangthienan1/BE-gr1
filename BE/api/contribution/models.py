from django.db import models
from ..info.models import Info
# Create your models here. ok


class Contribution(models.Model):
    contribution_id = models.AutoField(primary_key=True)
    sub_date = models.TimeField(auto_now_add=True)
    aprv_date = models.DateTimeField(blank=True, null=True)
    status = models.BooleanField(default=False)
    img = models.ImageField(upload_to='images/', blank=True, null=True)
    document = models.FileField(upload_to=None)
    infoID = models.ForeignKey(Info, on_delete=models.CASCADE)
    pass

    def __str__(self):
        return self.contributionID
