from django.core.exceptions import ValidationError
from django.db import models

from budbua.utils.mixins import TimeStampable
from users.models import User


class Ad(TimeStampable):
    class Meta:
        ordering = ('-created_at',)

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

    minimum_bid = models.IntegerField(
        verbose_name='minimum bid',
        default=0,
    )

    zip_code = models.CharField(
        verbose_name='zip code',
        max_length=4,
        null=True, blank=True,
    )

    image_string = models.TextField(
        verbose_name='image string',
        null=True, blank=True,
    )

    @property
    def maximum_bid(self):
        return self.bids.first().value if self.bids.count() else None

    @property
    def num_bids(self):
        return self.bids.count()

    @property
    def first_name(self):
        return self.owner.first_name

    @property
    def last_name(self):
        return self.owner.last_name

    @property
    def email(self):
        return self.owner.email

    @property
    def highest_bidder(self):
        if self.bids.count() != 0:
            bidder = self.bids.first().bidder
            user = {
                "id": bidder.id,
                "name": bidder.name,
            }
            return user
        else:
            return None


class Bid(TimeStampable):
    class Meta:
        ordering = ('-created_at',)

    def __str__(self):
        return f'Bid(bidder={self.bidder}, ad={self.ad.title}, value={self.value})'

    bidder = models.ForeignKey(
        'users.User',
        verbose_name='bidder',
        on_delete=models.CASCADE,
        related_name='bids',
        null=True, blank=True,
    )

    ad = models.ForeignKey(
        'auctions.Ad',
        verbose_name='ad',
        on_delete=models.CASCADE,
        related_name='bids',
    )

    value = models.IntegerField(
        verbose_name='value',
    )

    # Implements custom validation
    def clean(self, *args, **kwargs):
        if self.bidder == self.ad.owner:
            raise ValidationError('Bidder and owner can not be the same person')
        super(Bid, self).clean(*args, **kwargs)

    def save(self, *args, **kwargs):
        self.full_clean()
        super(Bid, self).save(*args, **kwargs)
