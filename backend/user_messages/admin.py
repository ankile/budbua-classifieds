from django.contrib import admin

# Register your models here.
from user_messages.models import Message, Chat


@admin.register(Chat)
class AdAdmin(admin.ModelAdmin):
    pass


@admin.register(Message)
class BidAdmin(admin.ModelAdmin):
    pass
