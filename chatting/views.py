# chatting/views.py

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from dotenv import load_dotenv
from openai import OpenAI
import os
from .models import Conversation
from .decorators import daily_limit
from chatting.serializers import ConversationSerializer

load_dotenv()
client = OpenAI(
    api_key=os.environ['OPENAI_API_KEY'],
)

class ChatbotView(APIView):
    permission_classes = [IsAuthenticated]
    
    def dispatch(self, request, *args, **kwargs):
        response = super().dispatch(request, *args, **kwargs)
        return response
    
    def get(self, request, *args, **kwargs):
        conversations = Conversation.objects.filter(user=request.user).values()
        return Response(list(conversations))
    
    @daily_limit
    def post(self, request, *args, **kwargs):
        user = request.user
        prompt = request.data.get('prompt')
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
            conversation_db = Conversation(user=user, prompt=prompt, response=response)
            conversation_db.save()

            conversation = {'prompt': prompt, 'response': response}
            # 대화 기록에 새로운 응답 추가
            session_conversations.append(conversation)
            request.session['conversations'] = session_conversations

            return Response(conversation)

        return Response({"error": "No prompt provided"}, status=status.HTTP_400_BAD_REQUEST)

chat_room = ChatbotView.as_view()

class ChatHistoryView(APIView):
    def get(self, request, *args, **kwargs):
        conversations = Conversation.objects.filter(user=request.user)
        serialized_conversations = ConversationSerializer(conversations, many=True)
        return Response(serialized_conversations.data)
    
chat_history = ChatHistoryView.as_view()
