# chatting > urls.py

from django.urls import path
from . import views

urlpatterns = [
    path('', views.chat_room, name='chat_room'),
    path('history/', views.chat_history, name='chat_history')
]
