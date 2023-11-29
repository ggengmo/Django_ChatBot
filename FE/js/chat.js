(function () {
    const titleElement = document.querySelector('.top_menu .title');
    const email = localStorage.getItem('email');
    titleElement.textContent += ` - ${email}`;
    
    let Message;
    Message = function (arg) {
        this.text = arg.text, this.message_side = arg.message_side;
        this.draw = function (_this) {
            return function () {
                let message;
                message = document.querySelector('.message_template li.message').cloneNode(true);
                message.classList.add(_this.message_side);
                message.querySelector('.text').innerText = _this.text;
                let messageList = document.querySelector('.messages');
                messageList.append(message);
                
                setTimeout(function () {
                    message.classList.add('appeared');
                    messageList.scrollTop = messageList.scrollHeight;
                }, 0);
            };
        }(this);
        return this;
        
    };
    const buttonClassNames = ['close', 'minimize', 'maximize'];

    buttonClassNames.forEach(className => {
        document.querySelector(`.button.${className}`).addEventListener('click', function() {
            switch (className) {
                case 'close':
                    // 로그아웃 요청 보내기
                    fetch('http://127.0.0.1:8000/logout/', {
                        method: 'POST',
                        headers: {
                            'Content-Type': 'application/json',
                            'Authorization': `Bearer ${localStorage.getItem('jwt')}`
                        },
                        body: JSON.stringify({refresh_token: localStorage.getItem('refresh_token')})
                    })
                    .then(response => {
                        if (response.status === 205) {
                            // 로그아웃 성공, 로컬 스토리지 클리어 후 원래 있던 페이지로 이동
                            localStorage.clear();
                            window.location.href = 'http://127.0.0.1:5500/FE/chat.html';
                        } else {
                            // 로그아웃 실패, 에러 메시지 출력
                            console.error('Logout failed');
                        }
                    })
                    .catch(error => console.error('Error:', error));
                    break;
                case 'minimize':
                    // 회원가입 페이지로 이동
                    window.location.href = 'http://127.0.0.1:5500/FE/signup.html';
                    break;
                case 'maximize':
                    // 로그인 페이지로 이동
                    window.location.href = 'http://127.0.0.1:5500/FE/login.html';
                    break;
                default:
                    break;
            }
        });
    });
    fetch('http://127.0.0.1:8000/chatting/', {
        method: 'GET',
        headers: {
            'Content-Type': 'application/json',
            'Authorization': `Bearer ${localStorage.getItem('jwt')}`
        },
    })
    .then(response => response.json())
    .then(data => {
        console.log(data);
        let message_side = 'right';
        data.forEach(conversation => {
            let message = new Message({
                text: conversation.prompt,
                message_side: message_side,
                template: '.message_template'
            });
            message.draw();
            message_side = message_side === 'left' ? 'right' : 'left';
            message = new Message({
                text: conversation.response,
                message_side: message_side,
                template: '.message_template'
            });
            message.draw();
            message_side = message_side === 'left' ? 'right' : 'left';
        });
    })
    .catch((error) => {
        console.error('Error:', error);
    });
    function send() {
        let messageInput = document.querySelector('.message_input');
        let prompt = messageInput.value;
        messageInput.value = '';
        fetch('http://127.0.0.1:8000/chatting/', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
                'Authorization': `Bearer ${localStorage.getItem('jwt')}`
            },
            body: JSON.stringify({prompt: prompt})
        })
        .then(response => response.json())
        .then(data => {
            let message_side = 'right';
            let message = new Message({
                text: data.prompt,
                message_side: message_side,
                template: '.message_template'
            });
            message.draw();
            message_side = message_side === 'left' ? 'right' : 'left';
            message = new Message({
                text: data.response,
                message_side: message_side,
                template: '.message_template'
            });
            message.draw();
        })
        .catch((error) => {
            console.error('Error:', error);
        });
    }
    document.querySelector('.send_message').addEventListener('click', send);
    document.querySelector('.message_input').addEventListener('keydown', function (event) {
        if (event.key === 'Enter') {
            send();
        }
    });
})();
