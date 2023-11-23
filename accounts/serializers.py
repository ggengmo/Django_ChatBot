# accounts > serializers.py

from dj_rest_auth.registration.serializers import RegisterSerializer
from dj_rest_auth.serializers import LoginSerializer
from rest_framework import serializers
from rest_framework_simplejwt.tokens import RefreshToken

class CustomRegisterSerializer(RegisterSerializer):
    nickname = serializers.CharField(max_length=30)
    daily_chat_count = serializers.IntegerField(default=0)

    def get_cleaned_data(self):
        super(CustomRegisterSerializer, self).get_cleaned_data()

        return {
            'username': self.validated_data.get('username', ''),
            'password1': self.validated_data.get('password1', ''),
            'email': self.validated_data.get('email', ''),
            'nickname': self.validated_data.get('nickname', ''),
            'daily_chat_count': self.validated_data.get('daily_chat_count', 0)
        }

class CustomLoginSerializer(LoginSerializer):
    username = None
    
    def validate(self, attrs):
        data = super().validate(attrs)
        
        refresh = RefreshToken.for_user(self.user)
        data['refresh'] = str(refresh)
        data['access'] = str(refresh.access_token)
        
        return data
