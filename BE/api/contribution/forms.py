from django.core.mail import send_mail
from django import forms
from django.forms import fields
from .models import Contribution
from BE.api.contribution import models

class ContributionUploadForm(forms.ModelForm):
    class Meta:
        model = Contribution
        fields = '__all__'

send_mail(
    'New Contribution Notification',
    'A new contribution has been submitted within your faculty.\nPlease review within 14 days.',
    'no-reply@example.com',
    [''], # coordinator emails here
    fail_silently=False,
)