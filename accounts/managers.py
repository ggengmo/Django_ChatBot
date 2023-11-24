# accounts > managers.py

from django.contrib.auth.models import BaseUserManager

class CustomuserManager(BaseUserManager):
    def create_user(self, email, name, password=None):

        user = self.model(
            email=self.normalize_email(email),
            name=name,
        )

        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, name, password):
        user = self.create_user(
            email,
            name=name,
            password=password,
        )

        user.is_admin = True
        user.save(using=self._db)
        return user