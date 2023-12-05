# chatting > urls.py

from django.urls import path
from . import views

urlpatterns = [
    path('', views.chatlist, name='chatlist'),
    path('<int:pk>/', views.chatdetail, name='chatdetail'),
    path('<int:id>/chatbot/', views.chatroom, name='chatroom'),
]
