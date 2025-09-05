from fastapi import FastAPI
import os

app = FastAPI()

# Root route
@app.get("/")
def read_root():
    return {"message": "Cancer Q&A Bot Backend is running!"}

# Simple ask route
@app.get("/ask")
def ask_question(q: str):
    return {"answer": f"You asked: {q}"}

# Correct entry point for Railway
if __name__ == "__main__":
    import uvicorn
    port = int(os.environ.get("PORT", 8000))  # Railway ka PORT use karega
    uvicorn.run("main:app", host="0.0.0.0", port=port)
