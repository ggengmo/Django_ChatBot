fetch('http://localhost:8000/chatting/')
    .then(response => response.json())
    .then(data => {
        console.log(data);  // 추가
        let div = document.getElementById('conversations');
        data.forEach(conversation => {
            div.innerHTML += `<p>Prompt: ${conversation.prompt}</p>`;
            div.innerHTML += `<p>Response: ${conversation.response}</p>`;
            div.innerHTML += '<hr>';
        });
    })
    .catch((error) => {
        console.error('Error:', error);
    });
