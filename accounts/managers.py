# accounts > managers.py

from django.contrib.auth.base_user import BaseUserManager
from django.utils.translation import gettext_lazy as _

class CustomUserManager(BaseUserManager):
    
    def create_user(self, name, email, nickname, password, **extra_fields):
        if not name:
            raise ValueError(_('사용자 이름은 필수입니다!'))
        if not email:
            raise ValueError(_('이메일은 필수입니다!'))
        if not nickname:
            raise ValueError(_('닉네임은 필수입니다!'))
        email = self.normalize_email(email)
        user = self.model(name=name, email=email, nickname=nickname, **extra_fields)
        user.set_password(password)
        user.save()
        return user
    
    def create_superuser(self, name, email, nickname, password, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        extra_fields.setdefault('is_active', True)
        
        if extra_fields.get('is_staff') is not True:
            raise ValueError(_("슈퍼유저는 'is_staff'가 반드시 True여야 합니다!"))
        if extra_fields.get('is_superuser') is not True:
            raise ValueError(_("슈퍼유저는 'is_superuser'가 반드시 True여야 합니다!"))
        return self.create_user(name, email, nickname, password, **extra_fields)

