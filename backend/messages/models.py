from django.db import models

# Create your models here.


class Messages(models.Model):

    message_sender = models.ForeignKey(
        'users.User',
        verbose_name='message sender',
        on_delete=models.CASCADE()
    )

    message_receiver = models.ForeignKey(
        'users.User',
        verbose_name='message receiver',
        on_delete=models.CASCADE()
    )

    message = models.TextField(
        verbose_name='message',

    )

    message_sent_time = models.DateTimeField(
        verbose_name='message sent at'
    )