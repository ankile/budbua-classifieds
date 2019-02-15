from django.db import models

from budbua.utils.mixins import TimeStampable
from users.models import User


class Ad(TimeStampable):

    class Meta:
        ordering = ('-created_at', )

    def __str__(self):
        return f'Ad(owner={self.owner}, title="{self.title}")'

    owner = models.ForeignKey(
        User,
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

    bid_end_time = models.DateTimeField(
        verbose_name='bid end time',
    )

    zip_code = models.IntegerField(
        verbose_name='zip code',
        null=True, blank=True,
    )

    @property
    def maximum_bid(self):
        return self.bids.first().value if self.bids.count() else None

    @property
    def minimum_bid(self):
        return self.bids.last().value

    @property
    def num_bids(self):
        return self.bids.count() - 1

    @property
    def first_name(self):
        return self.owner.first_name

    @property
    def last_name(self):
        return self.owner.last_name

    @property
    def email(self):
        return self.owner.email


class Bid(TimeStampable):

    class Meta:
        ordering = ('-created_at', )

    def __str__(self):
        return f'Bid(bidder={self.bidder}, ad={self.ad.title}, value={self.value})'

    bidder = models.ForeignKey(
        'users.User',
        on_delete=models.CASCADE,
        related_name='bids',
        null=True, blank=True,
    )

    ad = models.ForeignKey(
        'auctions.Ad',
        on_delete=models.CASCADE,
        related_name='bids',
    )

    value = models.IntegerField(
        verbose_name='value',
    )
