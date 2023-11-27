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
    .then(response => response.json())
    .then(data => {
        console.log('Success:', data);
    })
    .catch((error) => {
        console.error('Error:', error);
    });
    })