// Send message when Enter key is pressed
document.getElementById("user-input").addEventListener("keypress", function(event) {

    if (event.key === "Enter") {
        sendMessage();
    }

});

async function sendMessage() {

    const input = document.getElementById("user-input");
    const chatBox = document.getElementById("chat-box");

    const message = input.value.trim();

    if (message === "") return;

    // User Message
    chatBox.innerHTML += `
        <div class="user">
            <strong>🧑 You</strong>
            <p>${message}</p>
        </div>
    `;

    input.value = "";

    // Typing animation
    chatBox.innerHTML += `
        <div class="bot" id="typing">
            <strong>🤖 ZAID Bot</strong>
            <p>Typing...</p>
        </div>
    `;

    chatBox.scrollTop = chatBox.scrollHeight;

    try {

        const response = await fetch("/chat", {

            method: "POST",

            headers: {
                "Content-Type": "application/json"
            },

            body: JSON.stringify({
                message: message
            })

        });

        const data = await response.json();

        // Remove typing animation
        document.getElementById("typing").remove();

        // Bot reply
        chatBox.innerHTML += `
            <div class="bot">
                <strong>🤖 ZAID Bot</strong>
                <p>${data.reply.replace(/\n/g, "<br>")}</p>
            </div>
        `;

    }

    catch(error){

        document.getElementById("typing").remove();

        chatBox.innerHTML += `
            <div class="bot">
                <strong>🤖 ZAID Bot</strong>
                <p>❌ Sorry, I couldn't connect to the server.</p>
            </div>
        `;

    }

    chatBox.scrollTop = chatBox.scrollHeight;

}
