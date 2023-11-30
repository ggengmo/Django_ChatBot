# chatting > views.py

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from dotenv import load_dotenv
from openai import OpenAI
import os
from .models import Conversation, ChatRoom
from .decorators import daily_limit
from chatting.serializers import ConversationSerializer, ChatRoomSerializer

load_dotenv()
client = OpenAI(
    api_key=os.environ['OPENAI_API_KEY'],
)

class ChatlistView(APIView):
    permission_classes = [IsAuthenticated]
    
    def post(self, request, *args, **kwargs):
        chatroom = ChatRoom.objects.create(user=request.user)
        chatroom.name = f'Chatroom {chatroom.id}'
        chatroom.save()
        serializer = ChatRoomSerializer(chatroom)
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    
    def get(self, request, *args, **kwargs):
        chatrooms = ChatRoom.objects.filter(user=request.user)
        serializer = ChatRoomSerializer(chatrooms, many=True)
        return Response(serializer.data)
    
    def delete(self, request, *args, **kwargs):
        chatroom_id = kwargs.get('id')
        chatroom = ChatRoom.objects.get(id=chatroom_id, user=request.user)
        chatroom.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    
    def patch(self, request, *args, **kwargs):
        chatroom_id = kwargs.get('id')
        chatroom = ChatRoom.objects.get(id=chatroom_id, user=request.user)
        serializer = ChatRoomSerializer(chatroom, data=request.data, partial=True) # partial=True for partial updates
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

chatlist = ChatlistView.as_view()

class ChatbotView(APIView):
    permission_classes = [IsAuthenticated]
    
    def dispatch(self, request, *args, **kwargs):
        response = super().dispatch(request, *args, **kwargs)
        return response
    
    def get(self, request, *args, **kwargs):
        chatroom_id = kwargs.get('id')
        chatroom = ChatRoom.objects.get(id=chatroom_id, user=request.user)
        conversations = chatroom.conversations.all().values()
        return Response(list(conversations))
    
    @daily_limit
    def post(self, request, *args, **kwargs):
        user = request.user
        prompt = request.data.get('prompt')
        chatroom_id = kwargs.get('id')
        chatroom = ChatRoom.objects.get(id=chatroom_id, user=request.user)
        
        if prompt:
            # 이전 대화 기록 가져오기
            session_conversations = request.session.get('conversations', [])
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

            # 대화 기록 DB에 저장
            conversation_db = Conversation(user=user, chatroom=chatroom, prompt=prompt, response=response)
            conversation_db.save()

            conversation = {'prompt': prompt, 'response': response}
            # 대화 기록에 새로운 응답 추가
            session_conversations.append(conversation)
            request.session['conversations'] = session_conversations

            return Response(conversation)

        return Response({"error": "No prompt provided"}, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, *args, **kwargs):
        chatroom_id = kwargs.get('id')
        chatroom = ChatRoom.objects.get(id=chatroom_id, user=request.user)
        chatroom.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    
    def patch(self, request, *args, **kwargs):
        chatroom_id = kwargs.get('id')
        chatroom = ChatRoom.objects.get(id=chatroom_id, user=request.user)
        serializer = ChatRoomSerializer(chatroom, data=request.data, partial=True) # partial=True for partial updates
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
chatroom = ChatbotView.as_view()
