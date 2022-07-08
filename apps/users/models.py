from django.contrib.auth.base_user import BaseUserManager
from django.contrib.auth.models import AbstractUser
from django.db import models
from django.utils.translation import gettext_lazy as _


from apps.core.models import AbstractBaseModel


class UserManager(BaseUserManager):

    def create_user(self, email, password=None):
        if not email or not password:
            raise ValueError('User must have an email address and password')

        email = email.lower()
        user = self.model(email=self.normalize_email(email))
        user.set_password(password)
        user.save()
        return user

    def create_superuser(self, email, password):
        email = email.lower()
        user = self.create_user(email, password=password)
        user.is_staff, user.is_superuser, user.is_active = True, True, True
        user.save()
        return user


class User(AbstractUser, AbstractBaseModel):

    class Role(models.IntegerChoices):
        ADMIN = '1', _('Admin')
        USER = '2', _('User')

    first_name = models.CharField(
        verbose_name='First Name',
        max_length=63,
        default='First Name'
    )
    last_name = models.CharField(
        verbose_name='Last Name',
        max_length=63,
        default='Last Name'
    )
    email = models.EmailField(
        verbose_name='Email Address',
        max_length=255,
        unique=True,
        blank=False,
        null=False
    )
    role = models.PositiveSmallIntegerField(
        choices=Role.choices,
        default=Role.USER
    )

    objects = UserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    @property
    def full_name(self):
        return f"{self.first_name} {self.last_name}"

    def __str__(self):
        return self.full_name
