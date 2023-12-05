# chatting > views.py

from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from rest_framework.permissions import IsAuthenticated
from .models import Conversation, ChatRoom
from .decorators import daily_limit
from chatting.serializers import ConversationSerializer, ChatRoomSerializer
from openai import OpenAI
from dotenv import load_dotenv
import os
from rest_framework.response import Response
from rest_framework import status

load_dotenv()
client = OpenAI(api_key=os.environ['OPENAI_API_KEY'])

class ChatRoomListCreateView(ListCreateAPIView):
    serializer_class = ChatRoomSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return ChatRoom.objects.filter(user=self.request.user)

    def perform_create(self, serializer):
        serializer.save(user=self.request.user, name=f'Chatroom {serializer.instance.id}')

chatlist = ChatRoomListCreateView.as_view()

class ChatRoomRetrieveUpdateDestroyView(RetrieveUpdateDestroyAPIView):
    serializer_class = ChatRoomSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return ChatRoom.objects.filter(user=self.request.user)

chatdetail = ChatRoomRetrieveUpdateDestroyView.as_view()

class ChatbotView(RetrieveUpdateDestroyAPIView):
    serializer_class = ConversationSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        chatroom_id = self.kwargs.get('id')
        return Conversation.objects.filter(chatroom__id=chatroom_id, chatroom__user=self.request.user)

    @daily_limit
    def perform_create(self, serializer):
        user = self.request.user
        prompt = self.request.data.get('prompt')
        chatroom_id = self.kwargs.get('id')
        chatroom = ChatRoom.objects.get(id=chatroom_id, user=self.request.user)
        if prompt:
            session_conversations = self.request.session.get('conversations', [])
            previous_conversations = [
                {"role": role, "content": content}
                for conversation in session_conversations
                for role, content in [("user", conversation['prompt']), ("assistant", conversation['response'])]
            ]
            previous_conversations.append({"role": "user", "content": prompt})
            model_engine = "gpt-3.5-turbo"
            completions = client.chat.completions.create(
                model=model_engine,
                messages=previous_conversations
            )
            response = completions.choices[0].message.content
            conversation_db = Conversation(user=user, chatroom=chatroom, prompt=prompt, response=response)
            conversation_db.save()
            conversation = {'prompt': prompt, 'response': response}
            session_conversations.append(conversation)
            self.request.session['conversations'] = session_conversations
            return Response(serializer.data)
        return Response({"error": "프롬프트가 제공되지 않았습니다."}, status=status.HTTP_400_BAD_REQUEST)
    
chatroom = ChatbotView.as_view()
