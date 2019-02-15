from django.db import models
from django.utils import timezone
from rest_framework.views import APIView


class TimeStampable(models.Model):
    created_at = models.DateTimeField(
        verbose_name='created at',
        default=timezone.now
    )

    updated_at = models.DateTimeField(
        verbose_name='updated at',
        default=timezone.now
    )

    class Meta:
        abstract = True

    def save(self, *args, **kwargs):
        self.updated_at = timezone.now()
        return super(TimeStampable, self).save(*args, **kwargs)


class ModelView(APIView):

    model = None

    def get_object(self, pk):

        obj = self.model.objects.get(pk=pk)
        self.check_object_permissions(self.request, obj)

        return obj
