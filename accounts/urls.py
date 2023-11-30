# accounts > urls.py

from django.urls import include, path
from . import views

urlpatterns = [
    path('signup/', views.signup, name='signup'),
    path('login/', views.login, name='login'),
    path('logout/', views.logout, name='logout'),
    path('refresh/', views.refresh_token, name='refresh_token'),
]