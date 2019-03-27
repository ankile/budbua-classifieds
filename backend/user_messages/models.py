from django.db import models

# Create your models here.

from budbua.utils.mixins import TimeStampable


class Chat(TimeStampable):
    class Meta:
        ordering = ('-updated_at',)

    users = models.ManyToManyField(
        'users.User',
        related_name='chats',
    )

    @property
    def latest_message(self):
        return self.messages.last().message if self.messages.exists() else ""

    @property
    def message_count(self):
        return self.messages.count()


class Message(TimeStampable):
    class Meta:
        ordering = ('-created_at',)

    sender = models.ForeignKey(
        'users.User',
        verbose_name='sender',
        on_delete=models.CASCADE
    )

    chat = models.ForeignKey(
        Chat,
        related_name='messages',
        on_delete=models.CASCADE
    )

    message = models.TextField(
        verbose_name='message',
    )

    def save(self, **kwargs):
        self.chat.save()

        # Call super method to make sure it is saved to database
        super().save(**kwargs)
