from django.contrib import admin
from .models import Comment


# Register your models here.


class CommentAdmin(admin.ModelAdmin):
    list_display = ('content', 'time', 'contribution_id', 'info_id')


admin.site.register(Comment, CommentAdmin)
