from django.core.validators import MinValueValidator, MaxValueValidator
from django.db import models


class Rating(models.Model):
    class Meta:
        unique_together = ('rating_giver', 'rating_receiver')

    rating_giver = models.ForeignKey(
        'users.User',
        verbose_name='rating giver',
        on_delete=models.CASCADE,
        related_name='given_ratings',
    )

    rating_receiver = models.ForeignKey(
        'users.User',
        verbose_name='rating receiver',
        on_delete=models.CASCADE,
        related_name='received_ratings',
    )

    rating = models.IntegerField(
        validators=[MinValueValidator(1), MaxValueValidator(5)]
    )
