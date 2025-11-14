# AI Model Implementation Guide for Cancer Q&A Bot

## Overview
Yeh guide tumhe step-by-step batayega ki kaise AI model create karein aur backend mein integrate karein.

## Phase 1: Requirements & Planning

### 1.1 What We Need to Build
- **Disease Prediction**: Symptoms se disease predict karna
- **Treatment Recommendation**: Disease ke liye treatment suggest karna
- **Q&A Chatbot**: Natural language mein questions answer karna
- **Severity Detection**: Emergency cases identify karna

### 1.2 Tech Stack Options

#### Option A: Simple ML Model (Beginner Friendly)
```
- scikit-learn for ML models
- pandas for data handling
- joblib for model saving
- NLTK/spaCy for text processing
```

#### Option B: Advanced AI (Production Ready)
```
- Hugging Face Transformers
- OpenAI GPT-4 API
- LangChain for orchestration
- Vector databases (FAISS/Pinecone)
```

#### Option C: Hybrid Approach (Recommended)
```
- scikit-learn for symptom classification
- Hugging Face for conversational AI
- Custom knowledge base for medical info
```

---

## Phase 2: Data Collection

### 2.1 Disease-Symptom Dataset
Tumhe yeh data chahiye:

```python
# Example structure
{
    "disease": "Lung Cancer",
    "symptoms": [
        "persistent cough",
        "chest pain",
        "shortness of breath",
        "coughing blood",
        "weight loss",
        "fatigue"
    ],
    "severity": "critical",
    "treatment": "Chemotherapy, Radiation, Surgery",
    "specialists": ["Oncologist", "Pulmonologist"]
}
```

### 2.2 Data Sources
1. **Kaggle Datasets**:
   - Disease Symptom Prediction Dataset
   - Medical Q&A Dataset
   - Cancer Symptoms Dataset

2. **Create Custom Dataset**:
   - Manually curate from reliable medical sources
   - WebMD, Mayo Clinic, NIH data
   - Indian medical databases

### 2.3 Dataset Files to Create
```
data/
├── diseases.json          # Disease information
├── symptoms_mapping.json  # Symptom to disease mapping
├── treatments.json        # Treatment protocols
├── qa_pairs.json         # Question-Answer pairs
└── training_data.csv     # ML training data
```

---

## Phase 3: Model Development

### 3.1 Simple Symptom Checker (Start Here)

```python
# ml_model/symptom_checker.py

import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.naive_bayes import MultinomialNB
import joblib
import json

class SymptomChecker:
    def __init__(self):
        self.vectorizer = TfidfVectorizer(max_features=500)
        self.model = MultinomialNB()
        self.disease_info = {}
        
    def load_data(self, csv_path='data/training_data.csv'):
        """Load training data"""
        df = pd.read_csv(csv_path)
        return df
    
    def train(self, df):
        """Train the model"""
        # Prepare features (symptoms text)
        X = self.vectorizer.fit_transform(df['symptoms'])
        # Labels (disease names)
        y = df['disease']
        
        # Train
        self.model.fit(X, y)
        
        # Save model
        joblib.dump(self.vectorizer, 'models/vectorizer.pkl')
        joblib.dump(self.model, 'models/disease_classifier.pkl')
        
    def predict(self, symptoms_text):
        """Predict disease from symptoms"""
        # Transform input
        X = self.vectorizer.transform([symptoms_text])
        
        # Predict
        disease = self.model.predict(X)[0]
        probability = self.model.predict_proba(X).max()
        
        return {
            'disease': disease,
            'confidence': float(probability),
            'symptoms_analyzed': symptoms_text
        }
```

### 3.2 Advanced Conversational AI

```python
# ml_model/chatbot.py

from transformers import pipeline, AutoTokenizer, AutoModelForCausalLM
import torch

class MedicalChatbot:
    def __init__(self, model_name="microsoft/BioGPT-Large"):
        """Initialize medical chatbot with BioGPT"""
        self.tokenizer = AutoTokenizer.from_pretrained(model_name)
        self.model = AutoModelForCausalLM.from_pretrained(model_name)
        self.generator = pipeline(
            'text-generation',
            model=self.model,
            tokenizer=self.tokenizer
        )
        
    def get_response(self, question, context=""):
        """Generate response to medical question"""
        prompt = f"Patient Question: {question}\nMedical Response:"
        
        response = self.generator(
            prompt,
            max_length=200,
            num_return_sequences=1,
            temperature=0.7
        )
        
        return response[0]['generated_text']
```

### 3.3 Knowledge Base Setup

```python
# ml_model/knowledge_base.py

import json
from sentence_transformers import SentenceTransformer
import faiss
import numpy as np

class MedicalKnowledgeBase:
    def __init__(self):
        self.encoder = SentenceTransformer('all-MiniLM-L6-v2')
        self.index = None
        self.documents = []
        
    def load_knowledge(self, json_path='data/medical_knowledge.json'):
        """Load medical knowledge from JSON"""
        with open(json_path, 'r') as f:
            self.documents = json.load(f)
        
        # Create embeddings
        texts = [doc['content'] for doc in self.documents]
        embeddings = self.encoder.encode(texts)
        
        # Build FAISS index
        dimension = embeddings.shape[1]
        self.index = faiss.IndexFlatL2(dimension)
        self.index.add(embeddings.astype('float32'))
        
    def search(self, query, top_k=3):
        """Search relevant information"""
        query_embedding = self.encoder.encode([query])
        distances, indices = self.index.search(
            query_embedding.astype('float32'), 
            top_k
        )
        
        results = [self.documents[i] for i in indices[0]]
        return results
```

---

## Phase 4: Creating Training Data

### 4.1 Sample Training CSV

Create `data/training_data.csv`:

```csv
symptoms,disease,severity
"persistent cough chest pain shortness of breath",Lung Cancer,critical
"fatigue weight loss night sweats",Lymphoma,high
"breast lump pain discharge",Breast Cancer,critical
"headache vision problems nausea",Brain Tumor,critical
"blood in stool abdominal pain weight loss",Colon Cancer,high
"difficulty swallowing chest pain weight loss",Esophageal Cancer,high
```

### 4.2 Medical Knowledge JSON

Create `data/medical_knowledge.json`:

```json
[
    {
        "id": 1,
        "topic": "Lung Cancer Symptoms",
        "content": "Common symptoms of lung cancer include persistent cough, chest pain, shortness of breath, coughing up blood, and unexplained weight loss. Early detection is crucial.",
        "category": "symptoms"
    },
    {
        "id": 2,
        "topic": "Lung Cancer Treatment",
        "content": "Treatment options include surgery, chemotherapy, radiation therapy, targeted therapy, and immunotherapy. Treatment plan depends on cancer stage and patient health.",
        "category": "treatment"
    }
]
```

### 4.3 Diseases Database

Create `data/diseases.json`:

```json
{
    "lung_cancer": {
        "name": "Lung Cancer",
        "symptoms": [
            "persistent cough",
            "chest pain",
            "shortness of breath",
            "coughing blood",
            "weight loss"
        ],
        "severity": "critical",
        "treatment": "Surgery, Chemotherapy, Radiation, Targeted Therapy",
        "specialists": ["Oncologist", "Pulmonologist"],
        "emergency_action": "Visit emergency immediately if coughing blood or severe breathing difficulty"
    },
    "breast_cancer": {
        "name": "Breast Cancer",
        "symptoms": [
            "breast lump",
            "breast pain",
            "nipple discharge",
            "skin changes",
            "breast swelling"
        ],
        "severity": "critical",
        "treatment": "Surgery, Chemotherapy, Radiation, Hormone Therapy",
        "specialists": ["Oncologist", "Breast Surgeon"],
        "emergency_action": "Schedule immediate consultation with breast specialist"
    }
}
```

---

## Phase 5: Backend Integration

### 5.1 Update requirements.txt

```txt
fastapi==0.104.1
uvicorn==0.24.0
pydantic==2.4.2
scikit-learn==1.3.2
pandas==2.1.3
numpy==1.26.2
joblib==1.3.2
nltk==3.8.1
spacy==3.7.2
transformers==4.35.2
torch==2.1.1
sentence-transformers==2.2.2
faiss-cpu==1.7.4
python-multipart==0.0.6
```

### 5.2 Backend Structure

```
cancer-qabot-backend/
├── main.py
├── ml_model/
│   ├── __init__.py
│   ├── symptom_checker.py
│   ├── chatbot.py
│   ├── knowledge_base.py
│   └── utils.py
├── data/
│   ├── training_data.csv
│   ├── diseases.json
│   ├── medical_knowledge.json
│   └── qa_pairs.json
├── models/
│   ├── vectorizer.pkl
│   └── disease_classifier.pkl
└── static/
```

### 5.3 Updated main.py with AI Integration

```python
from fastapi import FastAPI, Request, HTTPException
from fastapi.staticfiles import StaticFiles
from fastapi.responses import FileResponse, JSONResponse
from pydantic import BaseModel
import os
from ml_model.symptom_checker import SymptomChecker
from ml_model.knowledge_base import MedicalKnowledgeBase
import json

app = FastAPI()

# Mount static files
app.mount("/static", StaticFiles(directory="static"), name="static")

# Initialize AI models
symptom_checker = SymptomChecker()
knowledge_base = MedicalKnowledgeBase()

# Load models on startup
@app.on_event("startup")
async def load_models():
    print("Loading AI models...")
    try:
        symptom_checker.load_models()
        knowledge_base.load_knowledge()
        print("✅ Models loaded successfully!")
    except Exception as e:
        print(f"⚠️ Warning: {e}")

# Request models
class SymptomsRequest(BaseModel):
    symptoms: str

class QuestionRequest(BaseModel):
    question: str
    context: str = ""

# Routes
@app.get("/")
async def root():
    return FileResponse("static/landing.html")

@app.get("/dashboard")
async def dashboard():
    return FileResponse("static/dashboard.html")

@app.get("/auth")
async def auth():
    return FileResponse("static/auth.html")

# AI Endpoints
@app.post("/predict")
async def predict_disease(request: SymptomsRequest):
    """Predict disease from symptoms"""
    try:
        result = symptom_checker.predict(request.symptoms)
        
        # Get treatment info
        disease_info = symptom_checker.get_disease_info(result['disease'])
        
        return {
            "disease": result['disease'],
            "confidence": result['confidence'],
            "severity": disease_info.get('severity', 'moderate'),
            "treatment": disease_info.get('treatment', ''),
            "specialists": disease_info.get('specialists', []),
            "emergency_action": disease_info.get('emergency_action', '')
        }
    except Exception as e:
        return {
            "error": str(e),
            "message": "Please provide more detailed symptoms for accurate prediction"
        }

@app.post("/chat")
async def chat(request: QuestionRequest):
    """Answer medical questions"""
    try:
        # Search knowledge base
        relevant_docs = knowledge_base.search(request.question)
        
        # Build context from relevant docs
        context = "\n".join([doc['content'] for doc in relevant_docs])
        
        return {
            "answer": context,
            "sources": relevant_docs,
            "confidence": 0.85
        }
    except Exception as e:
        return {
            "error": str(e),
            "answer": "I'm sorry, I couldn't process your question. Please try rephrasing."
        }

@app.get("/health")
async def health_check():
    return {
        "status": "healthy",
        "models_loaded": True,
        "version": "1.0.0"
    }

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
```

---

## Phase 6: Model Training Script

Create `train_model.py`:

```python
import pandas as pd
from ml_model.symptom_checker import SymptomChecker
import os

def prepare_training_data():
    """Prepare training data from diseases.json"""
    import json
    
    with open('data/diseases.json', 'r') as f:
        diseases = json.load(f)
    
    training_data = []
    for disease_key, info in diseases.items():
        symptoms_text = ' '.join(info['symptoms'])
        training_data.append({
            'symptoms': symptoms_text,
            'disease': info['name'],
            'severity': info['severity']
        })
    
    df = pd.DataFrame(training_data)
    df.to_csv('data/training_data.csv', index=False)
    return df

def train_models():
    """Train all AI models"""
    print("🚀 Starting model training...")
    
    # Create directories
    os.makedirs('models', exist_ok=True)
    os.makedirs('data', exist_ok=True)
    
    # Prepare data
    print("📊 Preparing training data...")
    df = prepare_training_data()
    print(f"✅ Created dataset with {len(df)} samples")
    
    # Train symptom checker
    print("🧠 Training symptom checker...")
    checker = SymptomChecker()
    checker.train(df)
    print("✅ Symptom checker trained successfully!")
    
    print("🎉 All models trained and saved!")

if __name__ == "__main__":
    train_models()
```

---

## Phase 7: Using External APIs (Alternative/Addition)

### 7.1 OpenAI Integration (Recommended for Production)

```python
# ml_model/openai_chatbot.py

import openai
import os
from typing import List, Dict

class OpenAIChatbot:
    def __init__(self, api_key: str = None):
        self.api_key = api_key or os.getenv("OPENAI_API_KEY")
        openai.api_key = self.api_key
        
        # Medical context system prompt
        self.system_prompt = """You are a medical AI assistant specialized in cancer-related queries. 
        Provide accurate, empathetic responses. Always recommend consulting healthcare professionals 
        for serious symptoms. Use simple language that patients can understand."""
        
    def chat(self, user_message: str, conversation_history: List[Dict] = None):
        """Generate response using GPT-4"""
        messages = [{"role": "system", "content": self.system_prompt}]
        
        if conversation_history:
            messages.extend(conversation_history)
        
        messages.append({"role": "user", "content": user_message})
        
        response = openai.ChatCompletion.create(
            model="gpt-4",
            messages=messages,
            temperature=0.7,
            max_tokens=500
        )
        
        return response.choices[0].message.content
```

### 7.2 Environment Variables

Create `.env` file:

```env
OPENAI_API_KEY=your_openai_api_key_here
HUGGINGFACE_TOKEN=your_hf_token_here
DATABASE_URL=postgresql://user:pass@localhost/cancer_qa
```

---

## Phase 8: Deployment Steps

### 8.1 Local Testing

```bash
# Install dependencies
pip install -r requirements.txt

# Download spaCy model
python -m spacy download en_core_web_sm

# Train models
python train_model.py

# Run server
python main.py
```

### 8.2 Production Deployment (Render/Railway)

```yaml
# render.yaml
services:
  - type: web
    name: cancer-qabot-api
    env: python
    buildCommand: "pip install -r requirements.txt && python train_model.py"
    startCommand: "uvicorn main:app --host 0.0.0.0 --port $PORT"
    envVars:
      - key: OPENAI_API_KEY
        sync: false
      - key: PYTHON_VERSION
        value: 3.11.0
```

---

## Summary: Step-by-Step Implementation

1. ✅ **Create data folder** with diseases.json
2. ✅ **Create ml_model folder** with Python files
3. ✅ **Update requirements.txt** with ML libraries
4. ✅ **Run train_model.py** to create ML models
5. ✅ **Update main.py** with AI endpoints
6. ✅ **Test locally** with symptom predictions
7. ✅ **Deploy to production** (Render/Railway)
8. ✅ **Monitor and improve** based on user feedback

## Next Steps

1. Collect more medical data for better accuracy
2. Add multilingual support (Hindi/English)
3. Implement user feedback loop
4. Add image analysis for medical reports
5. Integrate with hospital APIs
6. Add appointment booking system

---

**Important Notes:**
- Always add medical disclaimer
- Never replace real doctor consultation
- Focus on education and awareness
- Comply with medical data regulations (HIPAA, etc.)
- Regular model updates with latest medical knowledge
