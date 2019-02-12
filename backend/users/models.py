from django.contrib.auth.base_user import AbstractBaseUser
from django.contrib.auth.models import PermissionsMixin, UserManager
from django.db import models
from django.utils.translation import ugettext_lazy as _

from budbua.utils.mixins import TimeStampable


class User(AbstractBaseUser, PermissionsMixin, TimeStampable):
    username = models.CharField(
        _('username'),
        max_length=255,
        unique=True,
    )

    email = models.EmailField(
        _('email'),
        unique=True,
    )

    phone_number = models.CharField(
        verbose_name=_('phone number'),
        max_length=255,
        blank=True,
    )

    first_name = models.CharField(
        _('first name'),
        max_length=255,
        null=True, blank=True,
    )

    position = models.CharField(
        verbose_name=_('position at company'),
        max_length=255,
        blank=True,
    )

    last_name = models.CharField(
        _('last name'),
        max_length=255,
        null=True, blank=True,
    )

    is_active = models.BooleanField(
        _('is active'),
        default=True
    )

    is_staff = models.BooleanField(
        _('is staff'),
        default=False
    )

    is_superuser = models.BooleanField(
        _('is superuser'),
        default=False
    )

    objects = UserManager()

    USERNAME_FIELD = 'username'

    REQUIRED_FIELDS = ['email']
