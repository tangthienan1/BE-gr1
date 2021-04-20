from django.contrib import admin
from .models import Contribution

# Register your models here.

@admin.register(Contribution)
class ContributionAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'faculty', 'submission_date', 'status')
    list_filter = ('status', 'submission_date', 'approval_date', 'author', 'faculty', 'status')
    search_fields = ('title',)
    prepopulated_fields = {'slug':('title',)}
    raw_id_fields = ('author',)
    date_hierarchy = 'submission_date'
    ordering = ('status', 'submission_date')
