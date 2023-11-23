# accounts > urls.py

from django.urls import path, include
from .views import LoginView

urlpatterns = [
    path('', include('dj_rest_auth.urls')),
    path('signup/', include('dj_rest_auth.registration.urls')),
    path('login/', LoginView.as_view(), name='account_login'),
]
