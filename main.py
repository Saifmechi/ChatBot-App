from fastapi import FastAPI, WebSocket
from fastapi.responses import HTMLResponse
from fastapi import Request

app = FastAPI()

# Store WebSocket connections
websockets = []

@app.get("/")
async def read_root(request: Request):
    return HTMLResponse("""
        <html>
            <head>
                <title>Chatbot</title>
                <style>
                    body {
                        font-family: Arial, sans-serif;
                        margin: 20px;
                        background-color: #f0f0f0;
                    }

                    #chat-container {
                        max-width: 600px;
                        margin: auto;
                        border: 1px solid #ccc;
                        padding: 10px;
                        border-radius: 5px;
                        box-shadow: 0 0 10px rgba(0, 0, 0, 0.1);
                        background-color: #fff;
                        overflow-y: scroll; /* Add scrollbar for overflow */
                        max-height: 400px; /* Limit chat height */
                    }

                    .message {
                        margin: 10px;
                        padding: 10px;
                        border-radius: 5px;
                        max-width: 80%; /* Limit message width */
                    }

                    .user-message {
                        background-color: #e0f7fa;
                        text-align: right;
                        float: right;
                    }

                    .chatbot-message {
                        background-color: #f5f5f5;
                        text-align: left;
                        float: left;
                    }
                </style>
            </head>
            <body>
                <div id="chat-container">
                    <ul id="messages"></ul>
                    <form onsubmit="sendMessage(event)">
                        <input type="text" id="messageText" autocomplete="off" placeholder="Type your message..." />
                        <button>Send</button>
                    </form>
                </div>
                <script>
                    var ws = new WebSocket("ws://127.0.0.1:8000/ws/1");
                    ws.onmessage = function(event) {
                        var messages = document.getElementById("messages");
                        var message = document.createElement("li");
                        var content = document.createTextNode(event.data);

                        // Style user and chatbot messages differently
                        if (event.data.startsWith("Chatbot:")) {
                            message.className = "message chatbot-message";
                        } else {
                            message.className = "message user-message";
                        }

                        message.appendChild(content);
                        messages.appendChild(message);

                        // Scroll to the bottom of the chat container
                        messages.scrollTop = messages.scrollHeight;
                    };

                    function sendMessage(event) {
                        event.preventDefault();
                        var messageInput = document.getElementById("messageText");
                        ws.send(messageInput.value);

                        // Display user message on the right
                        var messages = document.getElementById("messages");
                        var userMessage = document.createElement("li");
                        userMessage.className = "message user-message";
                        var userContent = document.createTextNode("You: " + messageInput.value);
                        userMessage.appendChild(userContent);
                        messages.appendChild(userMessage);

                        // Scroll to the bottom of the chat container
                        messages.scrollTop = messages.scrollHeight;

                        messageInput.value = "";
                    }
                </script>
            </body>
        </html>
    """)


@app.websocket("/ws/{client_id}")
async def websocket_endpoint(websocket: WebSocket, client_id: int):
    await websocket.accept()
    websockets.append(websocket)

    try:
        while True:
            message = await websocket.receive_text()
            # Simulate a response from the chatbot
            bot_response = f"Chatbot: I received your message: {message}"
            await websocket.send_text(bot_response)
    except Exception as e:
        print(f"WebSocket Error: {e}")
    finally:
        websockets.remove(websocket)
