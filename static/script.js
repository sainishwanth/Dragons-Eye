function sendMessage() {
    const userMessage = document.getElementById('user-message').value;
    if (userMessage) {
        displayMessage(userMessage, 'user');

        fetch('/send_message', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json'
            },
            body: JSON.stringify({ message: userMessage })
        })
        .then(response => response.json())
        .then(data => {
            const responseMessage = data.message;
            displayMessage(responseMessage, 'received');
        });

        document.getElementById('user-message').value = '';
    }
}

function displayMessage(message, type) {
    const chatLog = document.getElementById('chat-log');
    const messageDiv = document.createElement('div');
    messageDiv.className = `message ${type}`;
    messageDiv.textContent = message;
    chatLog.appendChild(messageDiv);
}

document.getElementById('user-message').addEventListener('keyup', function(event) {
    if (event.key === 'Enter') {
        sendMessage(); 
    }
});

function retrieveAndDisplayMessages() {
    fetch('/get_messages', {
        method: 'GET',
    })
    .then(response => response.json())
    .then(data => {
        const messages = data.messages;
        messages.forEach(message => {
            displayMessage(message, 'received');
        });
    });
}

retrieveAndDisplayMessages();
