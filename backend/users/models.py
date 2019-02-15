from django.contrib.auth.base_user import AbstractBaseUser
from django.contrib.auth.models import PermissionsMixin
from django.db import models

from budbua.utils.managers import CustomUserManager
from budbua.utils.mixins import TimeStampable


class User(AbstractBaseUser, PermissionsMixin, TimeStampable):
    email = models.EmailField(
        verbose_name='email',
        unique=True,
    )

    first_name = models.CharField(
        verbose_name='first name',
        max_length=255,
        null=True, blank=True,
    )

    last_name = models.CharField(
        verbose_name='last name',
        max_length=255,
        null=True, blank=True,
    )

    is_active = models.BooleanField(
        verbose_name='is active',
        default=True
    )

    is_staff = models.BooleanField(
        verbose_name='is staff',
        default=False
    )

    is_superuser = models.BooleanField(
        verbose_name='is superuser',
        default=False
    )

    @property
    def name(self):
        return f'{self.first_name if self.first_name else ""}{" " + str(self.last_name)  if self.first_name else ""}' \
            if self.first_name or self.last_name else self.username

    objects = CustomUserManager()

    USERNAME_FIELD = 'email'
