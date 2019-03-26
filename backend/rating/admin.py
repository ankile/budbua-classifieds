from django.contrib import admin
from rating.models import Rating


# Register your models here.
@admin.register(Rating)
class RatingAdmin(admin.ModelAdmin):
    pass
