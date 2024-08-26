from django.db import models
from core.basemodel import BaseModel

# Create your models here.

from django.db import models
from django.contrib.auth.models import (
    BaseUserManager, AbstractBaseUser,
    PermissionsMixin
)



class UserManager(BaseUserManager):

    def create_user(self, email, full_name, password, **other_fields):
        """
        Creates and saves a User with the given email, date of
        birth and password.
        """

        user = self.model(
            email=email,
            full_name=full_name,
            is_active=True,
            **other_fields
        )

        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, password, **other_fields):

        other_fields.setdefault('is_staff', True)
        other_fields.setdefault('is_superuser', True)
        other_fields.setdefault('is_active', True)

        if other_fields.get('is_staff') is not True:
            raise ValueError('Superuser must be assigned to is_staff=True.')
        if other_fields.get('is_superuser') is not True:
            raise ValueError('Superuser must be assigned to is_superuser=True.')

        superUser = self.model(email=email, **other_fields)
        superUser.set_password(password)
        superUser.save()
        return superUser


class User(AbstractBaseUser, PermissionsMixin):
    full_name = models.CharField(max_length=255, blank=True, null=True)
    email = models.EmailField(verbose_name='email address', max_length=255, unique=True, blank=True, null=True)
    profile_picture = models.ImageField(
        upload_to='profile_picture',
        blank=True,
        null=True,
    )

    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=False)
    verified = models.BooleanField(default=False)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    objects = UserManager()

    USERNAME_FIELD = 'email'

    def __str__(self):
        return f"{self.pk} - {self.full_name}"

    def save(self, *args, **kwargs):
        if not self.full_name:
            self.full_name = self.email
        return super(User, self).save(*args, **kwargs)


class Otp(BaseModel):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='otp')
    otp = models.CharField(max_length=4)
    created_at = models.DateTimeField(auto_now_add=True)
    has_used = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.user.full_name} - {self.otp}"

