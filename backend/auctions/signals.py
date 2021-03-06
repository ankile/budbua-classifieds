from django.db.models.signals import post_save
from django.dispatch import receiver

from auctions.models import Ad, Bid


@receiver(post_save, sender=Ad)
def create_initial_department(sender, instance, created, **kwargs):
    if created:
        Bid.objects.create(
            bidder=instance.user,
            ad=instance,
            value=instance.minimum_bid
        )
