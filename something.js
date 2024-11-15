document.addEventListener("DOMContentLoaded", function() {
    var chatbox = document.getElementById("chatbox");
    var userInput = document.getElementById("userInput");
    var sendButton = document.getElementById("sendButton");
    var conversation = [];

    function saveChatToMarkdown() {
        var timestamp = new Date().toISOString();
        var filename = "conversation_" + timestamp + ".md";
        var content = "# Conversation\n\n";

        for (var i = 0; i < conversation.length; i++) {
            var message = conversation[i];
            content += "**" + message.sender + "**: " + message.content + "\n\n";

            if (message.response) {
                content += "**Assistant**: " + message.response + "\n\n";
            }
        }

        var element = document.createElement("a");
        element.href = "data:text/plain;charset=utf-8," + encodeURIComponent(content);
        element.download = filename;
        element.style.display = "none";
        document.body.appendChild(element);
        element.click();
        document.body.removeChild(element);

        console.log("Conversation saved to " + filename);
    }

    function addMessage(sender, content) {
        var messageElement = document.createElement("p");
        messageElement.innerHTML = "<strong>" + sender + ":</strong> " + content;
        chatbox.appendChild(messageElement);
    }

    function addUserMessage() {
        var userInputValue = userInput.value;
        if (userInputValue.trim() !== "") {
            addMessage("User", userInputValue);
            conversation.push({ sender: "User", content: userInputValue });
            userInput.value = "";
            scrollToBottom();
        }
    }

    function scrollToBottom() {
        chatbox.scrollTop = chatbox.scrollHeight;
    }

    userInput.addEventListener("keypress", function(event) {
        if (event.keyCode === 13) {
            event.preventDefault();
            sendButton.click();
        }
    });

    sendButton.addEventListener("click", function() {
        addUserMessage();

        // Call a function or API to get the assistant's response
        // For simplicity, let's assume the response is stored in a variable called 'response'
        var response = "Assistant's response goes here";

        addMessage("Assistant", response);
        conversation.push({ sender: "Assistant", response: response });
        scrollToBottom();
    });

    window.addEventListener("beforeunload", function() {
        if (conversation.length > 0) {
            saveChatToMarkdown();
        }
    });
});