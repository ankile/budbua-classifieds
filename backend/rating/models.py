from django.db import models

# Create your models here.
class Rating(models.Model):

    rating_giver = models.ForeignKey(
        'users.User',
        verbose_name='rating giver',
        on_delete=models.CASCADE()
    )

    rating_receiver = models.ForeignKey(
        'users.User',
        verbose_name='rating receiver',
        on_delete=models.CASCADE()
    )

    rating = models.IntegerField(
        max_value = 5,
        min_value = 1,
    )