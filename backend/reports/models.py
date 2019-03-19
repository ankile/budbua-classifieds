
from django.db import models

from budbua.utils.mixins import TimeStampable
from django.core.exceptions import ValidationError
from users.models import User
from auctions.models import Ad


class AdReport(TimeStampable):

    class Meta:
        ordering = ('-created_at', )

    def __str__(self):
        return f'AdReport(reporter={self.reporter}, ad="{self.ad}")'

    reporter = models.ForeignKey(
        User,
        verbose_name='reporter',
        on_delete=models.CASCADE
    )

    ad = models.ForeignKey(
        Ad,
        verbose_name='ad',
        on_delete=models.CASCADE
    )


class UserReport(TimeStampable):

    class Meta:
        ordering = ('-created_at', )

    def __str__(self):
        return f'UserReport(reporter={self.reporter}, reported="{self.reported}")'

    reporter = models.ForeignKey(
        User,
        verbose_name='reporter',
        on_delete=models.CASCADE
    )

    reported = models.ForeignKey(
        User,
        verbose_name='reported',
        on_delete=models.CASCADE
    )