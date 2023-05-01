from django.contrib.auth.base_user import BaseUserManager
from django.db import models
from django.contrib.auth.models import AbstractUser


class CustomUserManager(BaseUserManager):

    def create_user(self, username, password, **extra_fields):
        username = self.username
        user = self.model(username=username, **extra_fields)
        user.set_password(password)
        user.save()
        return user

    def create_superuser(self, username, password, **extra_fields):
        extra_fields.setdefault("is_staff", True)
        extra_fields.setdefault("is_superuser", True)

        if extra_fields.get("is_staff") is not True:
            raise ValueError("Superuser has to have is_staff being True")

        if extra_fields.get("is_superuser") is not True:
            raise ValueError("Superuser has to have is_superuser being True")

        return self.create_user(
            username=username,
            password=password,
            **extra_fields
        )


class CustomUser(AbstractUser):
    email = models.EmailField()
    speciality = models.CharField(
        max_length=100,
        verbose_name="Speciality",
        blank=True,
        null=True
    )
    username = models.CharField(
        max_length=150,
        unique=True,
        blank=True,
        null=True
    )
    is_confirmed = models.BooleanField(default=False)

    def __str__(self):
        return self.username
