from fastapi import FastAPI

app = FastAPI()

# sample dataset
qa_pairs = {
    "what is cancer": "Cancer is a disease where cells grow uncontrollably.",
    "what is chemotherapy": "Chemotherapy is a treatment using powerful drugs to kill fast-growing cells.",
    "what are symptoms of breast cancer": "Common symptoms include lump in breast, change in shape, or skin dimpling."
}

@app.get("/")
def home():
    return {"message": "Cancer Q&A Bot Backend is running!"}

@app.get("/ask")
def ask(q: str):
    q_lower = q.lower()
    if q_lower in qa_pairs:
        return {"answer": qa_pairs[q_lower]}
    else:
        return {"answer": "Sorry, I don’t have an answer for that yet."}
