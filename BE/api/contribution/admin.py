from django.contrib import admin
from .models import Contribution

# Register your models here.

@admin.register(Contribution)
class ContributionAdmin(admin.ModelAdmin):
    list_display = ('title', 'slug', 'author', 'approval_date', 'status')
    list_filter = ('status', 'submission_date', 'approval_date', 'author')
    search_fields = ('title',)
    prepopulated_fields = {'slug':('title',)}
    raw_id_fields = ('author',)
    date_hierarchy = 'approval_date'
    ordering = ('status', 'approval_date')