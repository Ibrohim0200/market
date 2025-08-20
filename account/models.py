from django.contrib.auth.models import AbstractUser
from django.db import models
from rest_framework.authtoken.models import Token
from .manager import UserManager
from common.models import BaseModel


class User(AbstractUser, BaseModel):
    username = models.CharField(max_length=150, unique=True)
    email = models.EmailField(unique=True)
    address = models.CharField(max_length=255, blank=True, null=False)
    phone = models.CharField(max_length=20, blank=True, null=False)

    ROLE_CHOICES = (
        ('user', 'User'),
        ('admin', 'Admin'),
    )
    role = models.CharField(max_length=10, choices=ROLE_CHOICES, default='user')

    EMAIL_FIELD = 'email'
    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = ["first_name", "last_name"]

    objects = UserManager()

    class Meta:
        db_table = 'users'
        verbose_name = "User"
        verbose_name_plural = "Users"
    @property
    def token(self):
        token = Token.objects.filter(user=self).first()
        if token:
            return token.key
        return Token.objects.create(user=self).key

    def __str__(self):
        return f"{self.username} ({self.role})"
