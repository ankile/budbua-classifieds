from django.db import models

from auctions.models import Ad
from budbua.utils.mixins import TimeStampable
from users.models import User


class AdReport(TimeStampable):
    class Meta:
        ordering = ('-created_at',)

    def __str__(self):
        return f'AdReport(reporter={self.reporter}, ad="{self.ad}")'

    reporter = models.ForeignKey(
        User,
        verbose_name='reporter',
        related_name='ads_reported',
        on_delete=models.CASCADE
    )

    ad = models.ForeignKey(
        Ad,
        verbose_name='ad',
        related_name='ad_reported',
        on_delete=models.CASCADE
    )


class UserReport(TimeStampable):
    class Meta:
        ordering = ('-created_at',)

    def __str__(self):
        return f'UserReport(reporter={self.reporter}, reported="{self.reported}")'

    reporter = models.ForeignKey(
        User,
        verbose_name='reporter',
        related_name='user_reported',
        on_delete=models.CASCADE
    )

    reported = models.ForeignKey(
        User,
        verbose_name='reported',
        related_name='self_reported',
        on_delete=models.CASCADE
    )
