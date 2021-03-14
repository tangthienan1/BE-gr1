from django.db import models

# Create your models here. ok


class Contribution(models.Model):
    contributionID = models.AutoField(primary_key=True)
    subDate = models.DateTimeField(blank=True)
    aprvDate = models.DateTimeField(blank=True)
    status = models.BooleanField(default=False)
    img = models.ImageField(upload_to=None)
    document = models.FileField(upload_to=None)
    infoID = models.ForeignKey('Info', on_delete=models.CASCADE)
    pass

    def __str__(self):
        return self.contributionID
