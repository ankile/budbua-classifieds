from django.contrib import admin

from reports.models import UserReport, AdReport


@admin.register(UserReport)
class UserReportAdmin(admin.ModelAdmin):
    pass


@admin.register(AdReport)
class AdReportAdmin(admin.ModelAdmin):
    pass

