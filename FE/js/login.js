document.getElementById("login-form").addEventListener("submit", function(event){
    event.preventDefault();

    let email = document.getElementById("email").value;
    let password = document.getElementById("your_pass").value;
    let currentURL = window.location.href;

    fetch('http://127.0.0.1:8000/accounts/login/', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
        },
        body: JSON.stringify({
            email: email,
            password: password,
        }),
    })
    .then(response => response.json())
    .then(data => {
        console.log('Success:', data);
        if (data.access_token) {
            localStorage.setItem('jwt', data.access_token);
            localStorage.setItem('refresh_token', data.refresh_token);
            localStorage.setItem('email', data.email);
            window.location.href = "http://127.0.0.1:5500/FE/chatlist.html";
            if (data.non_field_errors) {  // non_field_errors가 존재하는지 확인
                alert(data.non_field_errors);
            }
        }         
    })
    .catch((error) => {
        console.error('Error:', error);
    });
});
