# accounts > views.py

from dj_rest_auth.views import LoginView as BaseLoginView
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework.response import Response
from datetime import datetime
from django.conf import settings
from rest_framework import status
from rest_framework_simplejwt import settings as api_settings

class LoginView(BaseLoginView):
    def create_token(self, user):
        refresh = RefreshToken.for_user(user)
        return {
            'refresh': str(refresh),
            'access': str(refresh.access_token),
        }

    def login(self):
        self.user = self.serializer.validated_data['user']
        self.token = self.create_token(self.user)
        if getattr(settings, 'REST_SESSION_LOGIN', True):
            self.process_login()

    def get_response(self):
        serializer_class = self.get_response_serializer()
        serializer = serializer_class(instance=self.token, context={'request': self.request})

        response = Response(serializer.data, status=status.HTTP_200_OK)

        if getattr(settings, 'REST_USE_JWT', False):
            if getattr(settings, 'JWT_AUTH_COOKIE', None):
                expiration = (datetime.utcnow() + api_settings.JWT_EXPIRATION_DELTA)
                response.set_cookie(
                    settings.JWT_AUTH_COOKIE,
                    self.token['access'],
                    expires=expiration,
                    httponly=True
                )
        return response
