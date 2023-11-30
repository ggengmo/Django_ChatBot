# chatting > serializers.py

from rest_framework import serializers
from .models import Conversation, ChatRoom

class ConversationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Conversation
        fields = '__all__'
        
class ChatRoomSerializer(serializers.ModelSerializer):
    conversations = ConversationSerializer(many=True, read_only=True)

    class Meta:
        model = ChatRoom
        fields = ['id', 'user', 'name', 'conversations']