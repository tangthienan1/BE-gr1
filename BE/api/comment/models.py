from django.db import models
from ..info.models import Info
from ..contribution.models import Contribution
# Create your models here.


class Comment(models.Model):
    content = models.TextField(max_length=500)
    time = models.TimeField(auto_now_add=True)
    contributionID = models.ForeignKey('Contribution', on_delete=models.CASCADE,)
    infoID = models.ForeignKey('Info', on_delete=models.CASCADE,)
    pass

    def __str__(self):
        return self.content
