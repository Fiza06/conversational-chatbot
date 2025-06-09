# conversational-chatbot

Conversational AI Chatbot using Hugging Face + FastAPI

This project is a lightweight **Conversational AI chatbot** built using:
- `transformers` (Hugging Face) for natural language generation
- `FastAPI` for serving the model via an API
- Includes interactive documentation using Swagger UI


## 🚀 Features
- Uses Hugging Face's `pipeline("conversational")` with `DialoGPT-medium`
- Clean modular code: `model.py` (ML logic) & `app.py` (API server)


## 📁 Project Structure

ChatBot/
│
├── app.py           # FastAPI server
├── model.py         # Chatbot model logic
├── requirements.txt # Dependencies
└── README.md        # This file


## 🔧 Setup Instructions

### 1. Clone the repository
```bash
git clone https://github.com/Fiza06/conversational-chatbot.git
cd conversational-chatbot
````

### 2. Create and activate a virtual environment

```bash
python3 -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

## Run the Chatbot

### 1. Start the FastAPI server

```bash
uvicorn app:app --reload
```

