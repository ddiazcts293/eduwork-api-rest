from django.db import models
from django.contrib.auth.models import AbstractUser
from django_enum import EnumField
from users.managers import EduWorkUserManager

# Create your models here.

class EduWorkUser(AbstractUser):
    class Role(models.TextChoices):
        ADMIN = 'ADMIN', 'Administrator'
        STUDENT = 'STUDENT', 'Student'
        COMPANY = 'COMPANY', 'Company'

    role = EnumField(Role, default=Role.STUDENT)
    email = models.EmailField(unique=True)

    username = None
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    objects = EduWorkUserManager()

    def save(self, *args, **kwargs):
        if not self.pk and self.is_superuser:
            self.role = self.Role.ADMIN
        super().save(*args, **kwargs)
