from django.db import models
from django.contrib.auth.models import AbstractUser

from escritorio.models import Escritorio

class CustomUser(AbstractUser):
        escritorio = models.ForeignKey(
        Escritorio,
        on_delete=models.CASCADE,
        null=True,
        blank=True,
        related_name='usuarios'
    )
