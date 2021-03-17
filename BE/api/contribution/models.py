from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

# Create your models here.
class Contribution(models.Model):
    STATUS = (
        ('pending', 'Pending'),
        ('approved', 'Approved'),
        ('denied', 'Denied'),
    )

    title = models.CharField(max_length=250)
    slug = models.SlugField(max_length=250,unique_for_date='approval_date')
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='contributions')
    document = models.FileField(upload_to='documents/')
    image = models.ImageField(upload_to='images/')
    approval_date = models.DateTimeField(default=timezone.now)
    submission_date = models.DateTimeField(auto_now_add=True)
    update_date = models.DateTimeField(auto_now=True)
    status = models.CharField(max_length=20, choices=STATUS, default='pending')


    class Meta:
        ordering = ('-approval_date',) # sorting in descending order. most recent approved appear first

    def __str__(self):
        return self.title