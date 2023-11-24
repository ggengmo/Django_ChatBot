# accounts > serializers.py

from django.contrib.auth.models import User
from rest_framework import serializers
from django.contrib.auth import get_user_model


class CustomuserSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)

    class Meta:
        model = get_user_model()
        fields = ('id', 'email', 'password', 'name')

# 패스워드가 필요없는 다른 테이블에서 사용할 용도
class CustomuserInfoSerializer(serializers.ModelSerializer):

    class Meta:
        model = get_user_model()
        fields = ('id', 'email', 'name')