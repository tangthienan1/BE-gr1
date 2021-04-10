from django.contrib import admin
from .models import Contribution
# Register your models here.


class ContributionAdmin(admin.ModelAdmin):
    list_display = ('contribution_id', 'sub_date', 'aprv_date', 'status', 'img', 'document', 'infoID')


admin.site.register(Contribution, ContributionAdmin)
