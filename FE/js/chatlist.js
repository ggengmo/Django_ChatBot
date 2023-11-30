(function () {
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
                return refreshAccessToken().then(newAccessToken => {
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
            return;
        }
        return fetch('http://127.0.0.1:8000/accounts/refresh/', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
            },
            body: JSON.stringify({refresh: refreshToken})
        }).then(response => response.json()).then(data => {
            localStorage.setItem('jwt', data.access);
            return data.access;
        });
    }

    document.querySelector('.font-weight-bold').textContent = localStorage.getItem('email');

    document.querySelector('.btn.btn-primary.mr-2.active').addEventListener('click', function() {
        window.location.href = 'http://127.0.0.1:5500/FE/index.html';
    });

    document.querySelector('.btn.btn-primary.new').addEventListener('click', function() {
        if (localStorage.getItem('jwt')) {
            requestWithToken('http://127.0.0.1:8000/chatting/', 'POST', {})
                .then(data => {
                    let chatroomElement = document.querySelector('.mt-3').cloneNode(true);
                    let chatroomNameSpan = chatroomElement.querySelector('.chatroom-name');
                    chatroomNameSpan.textContent = 'Chatroom ' + data.id; // 채팅방의 이름을 서버의 응답으로 업데이트

                    chatroomElement.querySelector('.content-text-1').addEventListener('click', function() {
                        if (localStorage.getItem('jwt')) {
                            requestWithToken(`http://127.0.0.1:8000/chatting/${data.id}/`, 'DELETE')
                            .then(data => {
                                chatroomElement.remove();
                            })
                            .catch((error) => {
                                console.error('Error:', error);
                            });
                        }
                    });

                    document.querySelector('.card').append(chatroomElement);
                })
                .catch((error) => {
                    console.error('Error:', error);
                });
        }
    });

    if (localStorage.getItem('jwt')) {
        requestWithToken('http://127.0.0.1:8000/chatting/', 'GET')
        .then(data => {
            data.forEach(chatroom => {
                let chatroomTemplate = document.querySelector('#chatroom-template');
                let chatroomElement = chatroomTemplate.content.cloneNode(true);
                let chatroomDiv = chatroomElement.querySelector('div.d-flex.flex-column');
                let chatroomNameSpan = chatroomElement.querySelector('.chatroom-name');
                let chatroomEditIcon = document.createElement('i');
                let chatroomInfoDiv = document.createElement('div');

                chatroomNameSpan.textContent = chatroom.name || 'Chatroom ' + chatroom.id;
                chatroomEditIcon.classList.add('fa', 'fa-edit');

                chatroomNameSpan.addEventListener('click', function() {
                    window.location.href = `http://127.0.0.1:5500/FE/chatroom.html?id=${chatroom.id}`;
                });

                chatroomInfoDiv.style.display = 'flex';
                chatroomInfoDiv.appendChild(chatroomNameSpan);
                chatroomInfoDiv.appendChild(chatroomEditIcon);

                chatroomDiv.appendChild(chatroomInfoDiv);

                chatroomEditIcon.addEventListener('click', function() {
                    let newChatroomName = prompt('Enter new chatroom name');
                    if (newChatroomName) {
                        requestWithToken(`http://127.0.0.1:8000/chatting/${chatroom.id}/`, 'PATCH', {name: newChatroomName})
                        .then(data => {
                            chatroomNameSpan.textContent = newChatroomName; // 채팅방의 이름을 사용자가 입력한 것으로 업데이트
                            location.reload();
                        })
                        .catch((error) => {
                            console.error('Error:', error);
                        });
                    }
                });

                chatroomElement.querySelector('.content-text-1').addEventListener('click', function() {
                    if (localStorage.getItem('jwt')) {
                        requestWithToken(`http://127.0.0.1:8000/chatting/${chatroom.id}/`, 'DELETE')
                        .then(data => {
                            chatroomElement.remove();
                        })
                        .catch((error) => {
                            console.error('Error:', error);
                        });
                    }
                });

                document.querySelector('.card').append(chatroomElement);
            });
        })
        .catch((error) => {
            console.error('Error:', error);
        });
    }
})();
