# accounts > models.py

from django.db import models
from django.contrib.auth.models import AbstractBaseUser
from .managers import CustomuserManager

class CustomUser(AbstractBaseUser):
    email = models.EmailField(
        verbose_name='email',
        max_length=100,
        unique=True,
    )
    name = models.CharField(max_length=30)
    is_active = models.BooleanField(default=True)
    is_admin = models.BooleanField(default=False)

    objects = CustomuserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['name']

    def __str__(self):
        return self.email

    def has_perm(self, perm, obj=None):
        return self.is_admin

    def has_module_perms(self, app_label):
        return self.is_admin

    @property
    def is_staff(self):
        return self.is_admin
    
    class Meta:
        db_table = 'user'