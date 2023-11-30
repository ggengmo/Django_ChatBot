# chatting > urls.py

from django.urls import path
from . import views

urlpatterns = [
    path('', views.chatlist, name='chatlist'),
    path('<int:id>/', views.chatroom, name='chatroom'),
]
