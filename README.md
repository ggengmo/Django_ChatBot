# Django_ChatBot
- DRF_ChatBot
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

### 5.2 Accounts

### 5.3 Chatting
