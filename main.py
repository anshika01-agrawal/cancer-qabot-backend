from fastapi import FastAPI, Request
from fastapi.staticfiles import StaticFiles
from fastapi.responses import FileResponse, JSONResponse
from pydantic import BaseModel
import os

app = FastAPI()

# Mount static files
app.mount("/static", StaticFiles(directory="static"), name="static")

class SymptomsRequest(BaseModel):
    symptoms: str

# Serve landing page as root
@app.get("/")
async def root():
    return FileResponse("static/landing.html")

@app.get("/dashboard")
async def dashboard():
    return FileResponse("static/dashboard.html")

@app.get("/login")
async def login():
    return FileResponse("static/login.html")

@app.get("/signup")
async def signup():
    return FileResponse("static/signup.html")

# Legacy endpoint
@app.get("/ask")
async def ask(query: str = ""):
    return {"query": query}

# Disease prediction endpoint
@app.post("/predict")
async def predict(request: SymptomsRequest):
    """
    AI/ML endpoint for disease prediction based on symptoms
    
    NOTE: This is a placeholder. For production, implement:
    1. NLP preprocessing with spaCy or transformers
    2. ML model (scikit-learn, TensorFlow, PyTorch)
    3. Disease knowledge base with treatments
    4. Critical condition detection logic
    5. Doctor/hospital recommendation system
    """
    
    symptoms = request.symptoms.lower()
    
    # Simple keyword-based detection (placeholder for ML model)
    if any(word in symptoms for word in ['chest pain', 'shortness of breath', 'heart attack']):
        return JSONResponse({
            "disease": "Possible Cardiac Event",
            "severity": "critical",
            "treatment": "Seek immediate emergency care. Do not drive yourself.",
            "recommendations": [
                "Call emergency services (911)",
                "Chew aspirin if not allergic",
                "Find nearest emergency room"
            ]
        })
    
    elif any(word in symptoms for word in ['headache', 'fever', 'cough', 'cold']):
        return JSONResponse({
            "disease": "Common Cold or Flu",
            "severity": "mild",
            "treatment": "Rest, hydration, over-the-counter medications",
            "recommendations": [
                "Take acetaminophen for fever",
                "Drink plenty of fluids",
                "Get adequate rest",
                "Use throat lozenges for sore throat"
            ]
        })
    
    elif any(word in symptoms for word in ['stomach pain', 'nausea', 'vomiting', 'diarrhea']):
        return JSONResponse({
            "disease": "Gastroenteritis",
            "severity": "moderate",
            "treatment": "Hydration, bland diet, rest",
            "recommendations": [
                "Drink oral rehydration solution",
                "Eat bland foods (BRAT diet)",
                "Avoid dairy and fatty foods",
                "Consult doctor if symptoms persist > 2 days"
            ]
        })
    
    else:
        return JSONResponse({
            "message": "I need more information to help you. Please describe your symptoms in detail.",
            "suggestion": "Include: when symptoms started, severity, any triggers"
        })

# Correct entry point for Railway
if __name__ == "__main__":
    import uvicorn
    port = int(os.environ.get("PORT", 8000))
    uvicorn.run("main:app", host="0.0.0.0", port=port)
