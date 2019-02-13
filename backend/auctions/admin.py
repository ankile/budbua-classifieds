from django.contrib import admin

from auctions.models import Ad, Bid


@admin.register(Ad)
class AdAdmin(admin.ModelAdmin):
    pass


@admin.register(Bid)
class BidAdmin(admin.ModelAdmin):
    pass
