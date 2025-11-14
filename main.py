from fastapi import FastAPI, Request
from fastapi.staticfiles import StaticFiles
from fastapi.responses import FileResponse, JSONResponse
from pydantic import BaseModel
import os
from ml_model.symptom_checker import SymptomChecker
from ml_model.knowledge_base import MedicalKnowledgeBase

app = FastAPI()

# Mount static files
app.mount("/static", StaticFiles(directory="static"), name="static")

# Global ML models
symptom_checker = None
knowledge_base = None

@app.on_event("startup")
async def load_models():
    """Load ML models on application startup"""
    global symptom_checker, knowledge_base
    
    print("Loading ML models...")
    try:
        symptom_checker = SymptomChecker()
        symptom_checker.load_models()
        print("✓ Symptom checker loaded")
    except Exception as e:
        print(f"⚠ Symptom checker not available: {e}")
        print("  Run 'python train_model.py' to train the model first")
    
    try:
        knowledge_base = MedicalKnowledgeBase()
        knowledge_base.load_knowledge()
        print("✓ Medical knowledge base loaded")
    except Exception as e:
        print(f"⚠ Knowledge base not available: {e}")

class SymptomsRequest(BaseModel):
    symptoms: str

class ChatRequest(BaseModel):
    query: str

# Serve landing page as root
@app.get("/")
async def root():
    return FileResponse("static/landing.html")

@app.get("/dashboard")
async def dashboard():
    return FileResponse("static/dashboard.html")

@app.get("/login")
async def login():
    return FileResponse("static/auth.html")

@app.get("/signup")
async def signup():
    return FileResponse("static/auth.html")

@app.get("/auth")
async def auth():
    return FileResponse("static/auth.html")

# Legacy endpoint
@app.get("/ask")
async def ask(query: str = ""):
    return {"query": query}

# Disease prediction endpoint
@app.post("/predict")
async def predict(request: SymptomsRequest):
    """
    AI/ML endpoint for disease prediction based on symptoms
    """
    if not symptom_checker:
        return JSONResponse({
            "error": "Model not loaded",
            "message": "Please train the model first by running: python train_model.py"
        }, status_code=503)
    
    try:
        # Use ML model for prediction
        result = symptom_checker.predict(request.symptoms)
        
        # Get detailed disease information
        disease_info = symptom_checker.get_disease_info(result['disease'])
        
        return JSONResponse({
            "disease": result['disease'],
            "confidence": f"{result['confidence']:.1f}%",
            "alternative_diagnoses": [
                {"disease": d, "confidence": f"{c:.1f}%"} 
                for d, c in result['top_predictions'][1:4]  # Top 3 alternatives
            ],
            "severity": disease_info.get('severity', 'unknown'),
            "treatment": disease_info.get('treatment', 'Consult a healthcare provider'),
            "specialists": disease_info.get('specialists', []),
            "emergency_action": disease_info.get('emergency_action', ''),
            "disclaimer": "This is an AI-based preliminary assessment. Always consult qualified medical professionals for proper diagnosis and treatment."
        })
    
    except Exception as e:
        return JSONResponse({
            "error": "Prediction failed",
            "message": str(e)
        }, status_code=500)

@app.post("/chat")
async def chat(request: ChatRequest):
    """
    Medical Q&A endpoint using knowledge base
    """
    if not knowledge_base:
        return JSONResponse({
            "error": "Knowledge base not loaded",
            "message": "Medical knowledge base is not available"
        }, status_code=503)
    
    try:
        # Search knowledge base
        results = knowledge_base.search(request.query, top_k=3)
        
        if not results:
            return JSONResponse({
                "response": "I don't have specific information about that. Please consult with a healthcare professional for medical advice.",
                "sources": []
            })
        
        # Return top result as main response with sources
        main_result = results[0]
        
        return JSONResponse({
            "response": main_result['content'],
            "topic": main_result['topic'],
            "category": main_result['category'],
            "related_topics": [
                {"topic": r['topic'], "category": r['category']} 
                for r in results[1:3]
            ],
            "disclaimer": "This information is for educational purposes only. Consult healthcare professionals for medical advice."
        })
    
    except Exception as e:
        return JSONResponse({
            "error": "Chat failed",
            "message": str(e)
        }, status_code=500)

# Correct entry point for Railway
if __name__ == "__main__":
    import uvicorn
    port = int(os.environ.get("PORT", 8000))
    uvicorn.run("main:app", host="0.0.0.0", port=port)
