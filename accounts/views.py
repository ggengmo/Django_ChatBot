from rest_framework import status
from rest_framework.views import APIView
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework_simplejwt.exceptions import TokenError, InvalidToken
from rest_framework_simplejwt.views import TokenRefreshView
from rest_framework.generics import CreateAPIView
from django.contrib.auth import authenticate
from django.contrib.auth.models import update_last_login
from accounts.serializers import CustomuserSerializer
import logging
from .models import CustomRefreshToken, BlacklistedToken

class SignupView(CreateAPIView):
    serializer_class = CustomuserSerializer
    permission_classes = [AllowAny]

signup = SignupView.as_view()

class LoginView(APIView):
    permission_classes = [AllowAny]

    def post(self, request, *args, **kwargs):
        email = request.data.get('email')
        password = request.data.get('password')

        user = authenticate(email=email, password=password)
        if user is None:
            return Response({'message': '아이디 또는 비밀번호가 일치하지 않습니다.'}, status=status.HTTP_401_UNAUTHORIZED)

        refresh = CustomRefreshToken.for_user(user)
        update_last_login(None, user)

        return Response({
            'refresh_token': str(refresh),
            'access_token': str(refresh.access_token),
            'user_id': user.id,  # 유저 아이디를 클라이언트로 전송
            'email': user.email,  # 유저 이메일을 클라이언트로 전송
        }, status=status.HTTP_200_OK)

login = LoginView.as_view()

logger = logging.getLogger(__name__)
class LogoutView(APIView):
    def post(self, request, *args, **kwargs):
        try:
            refresh_token_str = request.data["refresh_token"]
            token = RefreshToken(refresh_token_str)
            BlacklistedToken.blacklist(token)
            return Response(status=status.HTTP_205_RESET_CONTENT)
        except Exception as e:
            logger.exception(e)
            return Response(status=status.HTTP_400_BAD_REQUEST)

logout = LogoutView.as_view()

class RefreshTokenView(TokenRefreshView):
    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)

        try:
            serializer.is_valid(raise_exception=True)
        except TokenError as e:
            raise InvalidToken(e.args[0])

        return Response(serializer.validated_data, status=status.HTTP_200_OK)

refresh_token = RefreshTokenView.as_view()