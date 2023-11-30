# Django_ChatBot
## 목차
[1. 목표와 기능](#1-목표와-기능)

[2. 개발 기술 및 환경](#2-개발-기술-및-환경)

[3. 프로젝트 구조와 개발 일정](#3-프로젝트-구조와-개발-일정)

[4. UI](#4-ui)

[5. 기능](#5-기능)

[6. 개발 이슈](#6-개발-이슈)

[7. 개발하면서 느낀점](#7-개발하면서-느낀점)

## 1. 목표와 기능
### 1.1 목표
- 사용자가 AI에게 여러가지를 물어서 답을 얻을 수 있는 ChatBot
### 1.2 기능
- OpenAI API를 통해 사용자가 원하는 질문 및 답변을 받을 수 있는 기능
## 2. 개발 기술 및 환경
### 2.1 개발 기술
#### FE
<div>
    <img src="https://img.shields.io/badge/html5-E34F26?style=for-the-badge&logo=html5&logoColor=white">
    <img src="https://img.shields.io/badge/css3-1572B6?style=for-the-badge&logo=css3&logoColor=white">
    <img src="https://img.shields.io/badge/javascript-F7DF1E?style=for-the-badge&logo=javascript&logoColor=white">
    <img src="https://img.shields.io/badge/bootstrap-7952B3?style=for-the-badge&logo=bootstrap&logoColor=white">
</div>

#### BE
<div>
    <img src="https://img.shields.io/badge/python-3776AB?style=for-the-badge&logo=python&logoColor=white">
    <img src="https://img.shields.io/badge/django-092E20?style=for-the-badge&logo=django&logoColor=white">
</div>

### 2.2 개발 환경
<div>
    <img src="https://img.shields.io/badge/visualstudio-007ACC?style=for-the-badge&logo=visualstudio&logoColor=white">
    <img src="https://img.shields.io/badge/github-181717?style=for-the-badge&logo=github&logoColor=white">
</div>

## 3. 프로젝트 구조와 개발 일정
### 3.1 프로젝트 Directory 구조
```
📦ChatGPT_DRF
 ┣ 📂accounts
 ┃ ┣ 📂migrations
 ┃ ┣ 📜admin.py
 ┃ ┣ 📜apps.py
 ┃ ┣ 📜managers.py
 ┃ ┣ 📜models.py
 ┃ ┣ 📜serializers.py
 ┃ ┣ 📜tests.py
 ┃ ┣ 📜urls.py
 ┃ ┣ 📜views.py
 ┃ ┗ 📜__init__.py
 ┣ 📂ChatBot
 ┃ ┣ 📜asgi.py
 ┃ ┣ 📜settings.py
 ┃ ┣ 📜urls.py
 ┃ ┣ 📜wsgi.py
 ┃ ┗ 📜__init__.py
 ┣ 📂chatting
 ┃ ┣ 📂migrations
 ┃ ┣ 📜admin.py
 ┃ ┣ 📜apps.py
 ┃ ┣ 📜decorators.py
 ┃ ┣ 📜models.py
 ┃ ┣ 📜serializers.py
 ┃ ┣ 📜tests.py
 ┃ ┣ 📜urls.py
 ┃ ┣ 📜views.py
 ┃ ┗ 📜__init__.py
 ┣ 📂main
 ┃ ┣ 📂migrations
 ┃ ┣ 📜admin.py
 ┃ ┣ 📜apps.py
 ┃ ┣ 📜models.py
 ┃ ┣ 📜tests.py
 ┃ ┣ 📜urls.py
 ┃ ┣ 📜views.py
 ┃ ┗ 📜__init__.py
 ┣ 📜.env
 ┣ 📜.gitignore
 ┣ 📜db.sqlite3
 ┣ 📜manage.py
 ┗ 📜README.md
```

### 3.2 프로젝트 URL 구조

|app: accounts |views 함수 이름|html 파일이름   |
|:------------|:------------|:------------|
|'signup/'     |signup        |signup.html   |
|'login/'      |login         |login.html    |
|'logout/'     |logout        |N/A           |
|'refresh/'    |refresh_token |N/A           |

|app: chatting  |views 함수 이름  |html 파일이름   |
|:-------------|:--------------|:------------|
|''|chatlist|chatlist.html|
|'<int:id>/'|chatroom|chatroom.html|

|app: main |views 함수 이름|html 파일이름|
|:--------|:------------|:---------|
|'/'       |index         |index.html|

### 3.3 개발 일정
<div>
  <img src="https://github.com/ggengmo/Django_ChatBot/assets/142369113/ccbdc2f5-2c6b-45f4-87a0-02e123d7be44" width="100%">
</div>
### 3.4 기능
<img src="https://github.com/ggengmo/Django_ChatBot/assets/142369113/5ae35365-8157-4737-acde-e2b458fe9c71" width="100%">

### 3.5 ERD(Entity-Relationship Diagram)
<img src="https://github.com/ggengmo/Django_ChatBot/assets/142369113/2979c618-209a-43a2-9c95-ccb45f22a52b" width="100%">

## 4. UI
|Main||
|-|-|
|<img src="https://github.com/ggengmo/Django_ChatBot/assets/142369113/2f774640-8f3b-4f4b-b722-2c0861ce7a24" width="100%">기본 메인|<img src="https://github.com/ggengmo/Django_ChatBot/assets/142369113/e361b46c-9f80-4aa0-b834-fd763d71b7a1" width="100%">로그인(chat, logout으로 변경) 시 메인|

|Accounts||
|-|-|
|<img src="https://github.com/ggengmo/Django_ChatBot/assets/142369113/18bd105b-6a18-4182-a468-69a647e5de00" width="100%">회원가입|<img src="https://github.com/ggengmo/Django_ChatBot/assets/142369113/2490c210-3275-4106-8cda-691d3aaf732f" width="100%">로그인|

|Chatting||
|-|-|
|<img src="https://github.com/ggengmo/Django_ChatBot/assets/142369113/5380bf40-9f6e-4a81-800c-ad020b48b04a" width="100%">로그인 시 채팅방 목록|<img src="https://github.com/ggengmo/Django_ChatBot/assets/142369113/97e1a841-8d79-47ab-9624-1ea6e63c77f8" width="100%">비로그인 시 채팅방 목록|
|<img src="https://github.com/ggengmo/Django_ChatBot/assets/142369113/9b3ee24f-856d-42de-bc05-46dbe61653d1" width="100%">로그인 시 채팅방|<img src="https://github.com/ggengmo/Django_ChatBot/assets/142369113/50befc99-c4c3-42ab-9e28-10ad5a51eb1f" width="100%">비로그인 시 채팅방|

## 5. 기능

### 5.1 Main
<img src="https://github.com/ggengmo/Django_ChatBot/assets/142369113/95cadc69-390e-4c2e-9d35-1451d66fdade" width="100%"><br>
- 메인페이지에서 로그인을 하면 채팅 목록과 로그아웃 버튼이 생기며 로그인 시 채팅 목록 페이지로 이동합니다.
<br>

### 5.2 Accounts
<img src="https://github.com/ggengmo/Django_ChatBot/assets/142369113/dffc1dda-f95d-40fe-8d83-df3fd3c016ee" width="100%"><br>
- 회원가입을 하면 로그인 페이지로 이동이 되며 로그인이 성공하면 채팅 목록 페이지로 이동합니다.
<br>

### 5.3 Chatting
<img src="https://github.com/ggengmo/Django_ChatBot/assets/142369113/1aaf8561-5023-45b5-b945-e314aeefb5cb" width="100%"><br>
- 로그인한 사용자는 New버튼을 누르면 채팅방이 생성됩니다.
<br>

<img src="https://github.com/ggengmo/Django_ChatBot/assets/142369113/e9c22ed0-e2c8-4918-bdff-adc0de2634d4"><br>
- 로그인한 사용자는 채팅방을 생성 후 생성된 채팅방 이름을 누르면 해당 채팅방으로 이동되며 채팅서비스를 이용할 수 있습니다.
<br>

<img src="https://github.com/ggengmo/Django_ChatBot/assets/142369113/baaaed50-35ac-4eb5-b22e-1e38c1a3e185"><br>
- 사용자가 이용한 채팅서비스는 DB에 저장되어 이전에 친 채팅을 확인을 할 수 있습니다.
<br>

<img src="https://github.com/ggengmo/Django_ChatBot/assets/142369113/df13bd39-b9b7-4847-9d33-385fb38752f2" width="100%"><br>
- 사용자는 여러 채팅방을 이용할 수 있으며 각각의 채팅방의 이름을 변경할 수 있습니다.
<br>

<img src="https://github.com/ggengmo/Django_ChatBot/assets/142369113/74192637-3f45-48da-a5dd-7a24325d1353" width="100%"><br>
- 만약 사용자가 더 이상 이용하지 않을 채팅방이 있다면 삭제를 할 수 있습니다.
<br>

<img src="https://github.com/ggengmo/Django_ChatBot/assets/142369113/06324cab-776a-4cb3-a1f4-b5f18aa87910" width="100%"><br>
- 만약 로그인을 하지 않은 상태로 채팅서비스에 접속하면 채팅서비스는 비활성화되어 있고 로그인을 하면 다시 활성화됩니다.
<br>

<img src="https://github.com/ggengmo/Django_ChatBot/assets/142369113/9c051948-1265-45d8-9c21-7102b51c9f84" width="100%"><br>
- 사용자마다 서로 다른 채팅방을 갖습니다.
<br>

## 6. 개발 이슈
### 6.1 데코레이터 사용시 ```'ChatbotView' object has no attribute 'user'``` 에러
```python
def daily_limit(func):
    def wrapper(request, *args, **kwargs):
        user = request.user
        count = cache.get(f'chatbot_count_{user.id}', 0)

        if count >= 5:
            return HttpResponse('하루에 5회만 이용 가능합니다.', status=429)

        response = func(request, *args, **kwargs)

        if request.method == 'POST':
            count += 1
            cache.set(f'chatbot_count_{user.id}', count, 86400)

        return response
    return wrapper
```
해당 코드에서 wrapper함수가 request 객체에 접근 시 오류가 발생하여 찾아보니 self.requset로 접근해야 한다는 것을 알고
```python
def daily_limit(func):
    def wrapper(self, *args, **kwargs):
        user = self.request.user
        count = cache.get(f'chatbot_count_{user.id}', 0)

        if count >= 5:
            return HttpResponse('하루에 5회만 이용 가능합니다.', status=429)

        response = func(self, *args, **kwargs)

        if self.request.method == 'POST':
            count += 1
            cache.set(f'chatbot_count_{user.id}', count, 86400)

        return response
    return wrapper
```
수정하여 해결하였습니다.

### 6.2 채팅방 이름을 추가한 후 생겼던 DB 에러 및 patch 에러
```python
class ChatRoom(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    name = models.CharField(max_length=50, default='Chatroom')

class Conversation(models.Model):
    chatroom = models.ForeignKey(ChatRoom, on_delete=models.CASCADE, related_name='conversations')
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    prompt = models.CharField(max_length=512)
    response = models.TextField()

    def __str__(self):
        return f'{self.prompt}: {self.response}'
```
기존 코드에서 chatroom에 name을 추가했더니 기존의 있던 채팅방들 때문에 migrate 오류가 발생하여 DB와 그전에 했던 migrations를 삭제하였습니다.

```python
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
```
그 후에 migrate를 한 후 patch요청을 하면 콘솔과 터미널에서는 patch가 성공했다고는 나오지만 이름수정이 안되어 확인해 보니 serializers.py에 name 필드를 추가 안 한 것을 알고 추가 후 patch를 성공하였습니다.

## 7. 개발하면서 느낀점
- 이번 프로젝트를 진행하면서 DRF를 처음 사용해보면서 처음이다보니 어려움을 많이 겪었습니다. 이를 통해 새로운 것을 배울 수 있는 기회가 되었고 특히, 기능 구현 과정에서 다양한 문제점을 마주하게 되었습니다. 이러한 문제를 해결하기 위해 다른 개발자들의 코드를 참조하거나 검색을 통해 필요한 정보를 찾는 등의 노력을 했습니다.
그러나, 오류 발생 원인과 해결 방법을 찾는 과정에서 오류의 원인을 파악하고, 이를 해결하는 데 상당한 시간이 소요되었습니다. 이 과정에서 제가 DRF에 대해 아직 완벽히 이해하지 못하고 있다는 것을 많이 깨달았습니다.
또한, DRF의 복잡성에 대한 처음 생각했던것보다 더 복잡하다는 경험을 했습니다. 이로 인해 처음 기획했던 일부 기능을 구현하지 못한 점은 아쉬움으로 남지만 이 경험은 저에게 어떤 부분을 더 학습하고 개선해야 하는지를 깨닫게 해주었습니다.









