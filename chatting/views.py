# chatting/views.py

from django.shortcuts import render
from django.views import View
from dotenv import load_dotenv
from openai import OpenAI
import os
from .models import Conversation

load_dotenv()
client = OpenAI(
    api_key=os.environ['OPENAI_API_KEY'],
)

class ChatbotView(View):
    def get(self, request, *args, **kwargs):
        conversations = request.session.get('conversations', [])
        return render(request, 'chatting.html', {'conversations': conversations})

    def post(self, request, *args, **kwargs):
        prompt = request.POST.get('prompt')
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
            conversation_db = Conversation(prompt=prompt, response=response)
            conversation_db.save()

            conversation = {'prompt': prompt, 'response': response}
            # 대화 기록에 새로운 응답 추가
            session_conversations.append(conversation)
            request.session['conversations'] = session_conversations

        return self.get(request, *args, **kwargs)

chat_room = ChatbotView.as_view()
