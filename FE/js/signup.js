document.getElementById("register-form").addEventListener("submit", function(event){
    event.preventDefault()

    let name = document.getElementById("name").value
    let email = document.getElementById("email").value
    let password = document.getElementById("pass").value

    fetch('http://127.0.0.1:8000/accounts/signup/', {
        method: 'POST',
        headers: {
        'Content-Type': 'application/json',
        },
        body: JSON.stringify({
        name: name,
        email: email,
        password: password,
        }),
    })
    .then(response => {
        console.log(response);
        if (!response.ok) {
            throw Error(response.statusText);
        }
        return response.json();
    })
    .then(data => {
        console.log('Success:', data);
        window.location.href = 'http://127.0.0.1:5500/FE/login.html';
    })
    .catch((error) => {
        console.error('Error:', error);
    });
    })