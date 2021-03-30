from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from ..info.models import Info

# Create your models here.
class Contribution(models.Model):
    STATUS = (
        ('pending', 'Pending'),
        ('approved', 'Approved'),
        ('denied', 'Denied'),
    )

    title = models.CharField(max_length=250)
    slug = models.SlugField(max_length=250,unique_for_date='approval_date')
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='contributions') # Temporarily use. Change to info later
    faculty = models.CharField(max_length=50)   # For temporarily use 
    document = models.FileField(upload_to='documents/', blank=True) # modify later 
    image = models.ImageField(upload_to='images/', blank=True) # modify later
    approval_date = models.DateTimeField(default=None, blank=True, null=True)
    submission_date = models.DateTimeField(auto_now_add=True)
    update_date = models.DateTimeField(auto_now=True)
    status = models.CharField(max_length=20, choices=STATUS, default='pending')


    class Meta:
        ordering = ('-approval_date',) # sorting in descending order. most recent approved appear first

    def __str__(self):
        return self.title
    
