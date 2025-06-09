
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from model import get_bot_response

app = FastAPI()

class ChatRequest(BaseModel):
    user_input: str

@app.get("/")
def root():
    return {"message": "Chatbot API is running. Use POST /chat"}

@app.post("/chat")
def chat(request: ChatRequest):
    try:
        bot_reply = get_bot_response(request.user_input)
        return {"bot_reply": bot_reply}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


if __name__ == "__main__":
    import uvicorn
    uvicorn.run("app:app", host="127.0.0.1", port=8000, reload=True)