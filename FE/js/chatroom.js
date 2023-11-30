(function () {
    function getChatroomIdFromUrl() {
        const urlParams = new URLSearchParams(window.location.search);
        return urlParams.get('id');
    }

    function requestWithToken(url, method, body = null) {
        const jwt = localStorage.getItem('jwt');
        return fetch(url, {
            method: method,
            headers: {
                'Content-Type': 'application/json',
                'Authorization': `Bearer ${jwt}`
            },
            body: body ? JSON.stringify(body) : null
        }).then(response => {
            if (response.status === 401) {
                // Access Token이 만료되었을 때
                return refreshAccessToken().then(newAccessToken => {
                    // 새로운 Access Token으로 요청을 다시 보냄
                    return requestWithToken(url, method, body);
                });
            } else {
                return response.json();
            }
        });
    }

    function refreshAccessToken() {
        const refreshToken = localStorage.getItem('refresh_token');
        if (!refreshToken) {
            // 로그아웃 상태에서는 refresh 요청을 보내지 않음
            return;
        }
        return fetch('http://127.0.0.1:8000/accounts/refresh/', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
            },
            body: JSON.stringify({refresh: refreshToken})
        }).then(response => response.json()).then(data => {
            // 새로운 Access Token을 로컬 스토리지에 저장
            localStorage.setItem('jwt', data.access);
            return data.access;
        });
    }

    const titleElement = document.querySelector('.top_menu .title');
    const email = localStorage.getItem('email');
    const jwt = localStorage.getItem('jwt');

    if (!email || !jwt) {
        titleElement.textContent = "로그인해야 이용하실 수 있습니다";
        document.querySelector('.send_message').disabled = true;
        document.querySelector('.message_input').disabled = true;
    } else {
        titleElement.textContent += ` - ${email}`;
    }

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
            const jwt = localStorage.getItem('jwt');
            if (jwt && (className === 'maximize')) {
                return;
            }
            switch (className) {
                case 'close':
                    console.log("Refresh token: ", localStorage.getItem('refresh_token'));

                    fetch('http://127.0.0.1:8000/accounts/logout/', {
                        method: 'POST',
                        headers: {
                            'Content-Type': 'application/json',
                            'Authorization': `Bearer ${localStorage.getItem('jwt')}`
                        },
                        body: JSON.stringify({refresh_token: localStorage.getItem('refresh_token')})
                    })
                    .then(response => {
                        if (response.status === 205) {
                            localStorage.removeItem('jwt'); 
                            localStorage.removeItem('refresh_token');
                            window.location.href = 'http://127.0.0.1:5500/FE/index.html';
                        } else {
                            console.error('Logout failed');
                        }
                    })
                    .catch(error => console.error('Error:', error));
                    break;
                case 'minimize':
                    window.location.href = 'http://127.0.0.1:5500/FE/chatlist.html';
                    break;
                case 'maximize':
                    window.location.href = 'http://127.0.0.1:5500/FE/login.html';
                    break;
                default:
                    break;
            }
        });
    });

    // 로그아웃 상태에서는 GET 요청을 보내지 않음
    if (localStorage.getItem('jwt')) {
        const chatroomId = getChatroomIdFromUrl();
        if (chatroomId) {
            requestWithToken(`http://127.0.0.1:8000/chatting/${chatroomId}/`, 'GET')
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
        }
    }

    // 요청을 보내는 코드
    function send() {
        let messageInput = document.querySelector('.message_input');
        let prompt = messageInput.value;
        messageInput.value = '';
        const chatroomId = getChatroomIdFromUrl();
        if (!localStorage.getItem('jwt') || !chatroomId) {
            return;
        }
        requestWithToken(`http://127.0.0.1:8000/chatting/${chatroomId}/`, 'POST', {prompt: prompt})
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
