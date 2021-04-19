import os.path

from django.db import models
from django.db.models.fields.files import FileField

from ..faculty.models import Faculty
from ..info.models import Info
from .validators import FileValidator

class Contribution(models.Model):
    IMAGE_EXTENSION = ['.jpg', '.jpeg', '.png']
    DOCUMENT_EXTENSION = ['.doc', '.docx', '.pdf']
    STATUS = (
        ('pending', 'Pending'),
        ('approved', 'Approved'),
        ('denied', 'Denied'),
    )

    def get_path(instance, filename):
        file_ext = os.path.splitext(filename)[1]
        if file_ext in Contribution.IMAGE_EXTENSION:
            file_path = "images/"
        if file_ext in Contribution.DOCUMENT_EXTENSION:
            file_path = "documents/"
        return file_path

    author = models.ForeignKey(Info, 
                               on_delete=models.CASCADE, 
                               related_name='contributions')
    title = models.CharField(max_length=255)
    description = models.TextField()
    faculty = models.ForeignKey(Faculty,
                                on_delete=models.CASCADE,
                                related_name='contributions')
    slug = models.SlugField(max_length=255,unique_for_date='approval_date') 
    file = models.FileField(upload_to=get_path,
                            validators=[FileValidator(allowed_extensions=['doc', 'docx', 'pdf', 'png', 'jpg', 'jpeg'],
                                                      max_size=20*1024*2014)])
    approval_date = models.DateTimeField(default=None, blank=True, null=True)
    submission_date = models.DateTimeField(auto_now_add=True)
    update_date = models.DateTimeField(auto_now=True)
    status = models.CharField(max_length=10, 
                              choices=STATUS, 
                              default='pending')

    class Meta:
        ordering = ('-approval_date',) # sorting in descending order. most recent approved appear first

    def __str__(self):
        return self.title

