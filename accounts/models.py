# accounts > models.py

from django.contrib.auth.models import AbstractUser
from django.db import models
from .managers import CustomUserManager

class CustomUser(AbstractUser):
    nickname = models.CharField(max_length=30)
    daily_chat_count = models.IntegerField(default=0)
    
    objects = CustomUserManager()

