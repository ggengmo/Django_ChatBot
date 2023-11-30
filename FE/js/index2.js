window.addEventListener('load', function() {
    const jwt = localStorage.getItem('jwt');

    const loginButton = document.querySelector('#login');
    const signupButton = document.querySelector('#signup');
    const logoutButton = document.querySelector('#logout');
    const chatButton = document.querySelector('#chatroom');

    if (jwt) {
        // 로그인 상태일 때
        loginButton.style.display = 'none';
        signupButton.style.display = 'none';
        logoutButton.style.display = 'inline-block';
        chatButton.style.display = 'inline-block';
    } else {
        // 로그인 상태가 아닐 때
        loginButton.style.display = 'inline-block';
        signupButton.style.display = 'inline-block';
        logoutButton.style.display = 'none';
        chatButton.style.display = 'none';
    }

    logoutButton.addEventListener('click', function() {
        // 로그아웃 요청 보내기
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
                // 로그아웃 성공, 로컬 스토리지 클리어 후 원래 있던 페이지로 이동
                localStorage.clear();
                window.location.href = 'http://127.0.0.1:5500/FE/index.html';
            } else {
                // 로그아웃 실패, 에러 메시지 출력
                console.error('Logout failed');
            }
        })
        .catch(error => console.error('Error:', error));
    });
});
