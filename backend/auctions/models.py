from django.db import models

from budbua.utils.mixins import TimeStampable


class Ad(TimeStampable):

    class Meta:
        ordering = ('-created_at', )

    def __str__(self):
        return f'Ad(owner={self.owner}, title="{self.title}")'

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

    bid_end_time = models.DateTimeField(
        verbose_name='bid end time',
    )

    minimum_bid = models.IntegerField(
        verbose_name='minimum bid',
        default=0,
    )

    @property
    def maximum_bid(self):
        return self.bids.first().value if self.bids.count() else None

    @property
    def num_bids(self):
        return self.bids.count()


class Bid(TimeStampable):

    class Meta:
        ordering = ('-created_at', )

    def __str__(self):
        return f'Bid(bidder={self.bidder}, ad={self.ad.title}, value={self.value})'

    bidder = models.ForeignKey(
        'users.User',
        on_delete=models.CASCADE,
        related_name='bids',
    )

    ad = models.ForeignKey(
        'auctions.Ad',
        on_delete=models.CASCADE,
        related_name='bids',
    )

    value = models.IntegerField(
        verbose_name='value',
    )
