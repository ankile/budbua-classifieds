from django.db import models


class Ad(models.Model):

    owner = models.ForeignKey(
        'users.User',
        verbose_name='owner',
        related_name='ads',
        on_delete=models.CASCADE,
    )

    title = models.CharField(
        verbose_name='title',
        max_length=255,
    )

    description = models.TextField(
        verbose_name='description',
    )

    minimum_bid = models.IntegerField(
        verbose_name='minimum bid',
        default=0,
    )

    bid_end_time = models.DateTimeField(
        verbose_name='bid end time',
    )


class Bid(models.Model):

    bidder = models.OneToOneField(
        'users.User',
        on_delete=models.CASCADE,
        related_name='bids',
    )

    ad = models.OneToOneField(
        'auctions.Ad',
        on_delete=models.CASCADE,
        related_name='bids',
    )
