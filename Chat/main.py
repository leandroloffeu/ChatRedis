from fastapi import FastAPI, WebSocket, WebSocketDisconnect
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
import redis



app = FastAPI()
with open("../chat/index.html","r") as file: html = file.read()
app = FastAPI()
app.mount("/static", StaticFiles(directory="static"), name="static")
app = FastAPI()
redis_client = redis.Redis(host="localhost", port=6379)  




class ConnectionManager:
    def __init__(self):
        self.active_connections: list[WebSocket] = []

    async def connect(self, websocket: WebSocket):
        await websocket.accept()
        self.active_connections.append(websocket)

    def disconnect(self, websocket: WebSocket):
        self.active_connections.remove(websocket)

    async def send_personal_message(self, message: str, websocket: WebSocket):
        await websocket.send_text(message)

    async def broadcast(self, message: str):
        for connection in self.active_connections:
            await connection.send_text(message)


manager = ConnectionManager()


@app.get("/")
async def get():
    return HTMLResponse(html)


@app.websocket("/ws/{client_id}")
async def websocket_endpoint(websocket: WebSocket, client_id: int):
    await manager.connect(websocket)
    try:
        while True:
            data = await websocket.receive_text()

            # Save message to Redis with a key (e.g., user ID or timestamp)
            redis_client.set(f"chat:{client_id}", data)

            # ... other message processing ...
    except WebSocketDisconnect:
        manager.disconnect(websocket)
        await manager.broadcast(f"USUARIO #{client_id} SAIU DA SALA.")
