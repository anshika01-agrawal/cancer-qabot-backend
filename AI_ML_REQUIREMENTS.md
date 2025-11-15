# AI/ML Requirements & API Integration Guide

## 🎯 Quick Start: Choose Your AI Backend

You have 2 options for creating an intelligent AI chatbot:

### Option A: Use External AI API (RECOMMENDED ⭐)
**Best for**: Smart, conversational responses  
**Needs**: API key (free tier available)  
**Setup time**: 5 minutes

### Option B: Use Local ML Model (CURRENT)
**Best for**: Offline operation, no API costs  
**Already working**: Yes ✅  
**Limitation**: Less intelligent, template-based responses

---

## 🚀 External AI API Options (Choose One)

### 1. Google Gemini (RECOMMENDED - FREE)

**Why Choose This?**
- ✅ FREE tier: 60 requests/minute
- ✅ No credit card required
- ✅ Good medical knowledge
- ✅ Easy setup

**Get API Key:**
1. Visit: https://ai.google.dev/
2. Click "Get API Key" → "Create API key"
3. Sign in with Google
4. Copy key (starts with `AIzaSy...`)

**Cost:**
- Free tier: 60 requests/min
- Paid: $0.001 per 1K tokens (very cheap)

---

### 2. OpenAI ChatGPT (BEST QUALITY)

**Why Choose This?**
- ✅ Most advanced AI
- ✅ Excellent medical reasoning
- ❌ Requires credit card ($5 minimum)

**Get API Key:**
1. Visit: https://platform.openai.com/signup
2. Add payment method
3. API Keys → Create new
4. Copy key (starts with `sk-...`)

**Cost:**
- GPT-3.5-turbo: $0.002 per 1K tokens
- GPT-4: $0.03 per 1K tokens

---

### 3. Hugging Face (OPEN SOURCE)

**Why Choose This?**
- ✅ Free tier
- ✅ Medical models (BioBERT)
- ✅ Privacy-focused

**Get API Key:**
1. Visit: https://huggingface.co/join
2. Settings → Access Tokens
3. Create token
4. Copy key (starts with `hf_...`)

**Cost:**
- Free tier available
- Pro: $9/month unlimited

---

## 📋 What You Need to Provide

**Just give me:**
1. **Which API?** (Gemini/OpenAI/Hugging Face)
2. **Your API Key** (I'll keep it secure in .env file)

**Example:**
```
"I want Gemini. My key is: AIzaSyAbC123..."
```

OR

```
"I want OpenAI. My key is: sk-abc123..."
```

---

## 🔧 What I'll Implement Once You Provide Key

### Files I'll Create:
```
.env                    # Your API key (secure, not committed to git)
.gitignore             # Protects .env from git
config.py              # Loads API key
ml_model/ai_chatbot.py # AI integration code
```

### Files I'll Update:
```
requirements.txt       # Add: google-generativeai or openai
main.py               # Update /chat endpoint with AI
```

### Features You'll Get:
1. ✅ **Smart Conversational AI** - Natural, context-aware responses
2. ✅ **Medical Knowledge** - Better than current database
3. ✅ **Empathetic Responses** - Understands user emotions
4. ✅ **Fallback System** - Uses local model if API fails
5. ✅ **Safety Filters** - Medical disclaimers included

---

## 📊 Comparison: Current vs AI-Powered

### Current System (Local ML)
**User:** "I have cough for 3 weeks"

**Bot Response:**
```
Disease: Lung Cancer
Confidence: 28.3%
Treatment: Surgery, chemotherapy, radiation...
Specialists: Oncologist, Pulmonologist
```
❌ Scary, mechanical, no context

---

### With AI API (Gemini/OpenAI)
**User:** "I have cough for 3 weeks"

**Bot Response:**
```
I understand you've been dealing with a persistent cough for 3 weeks. 
While there are many possible causes ranging from minor infections to 
more serious conditions, a cough lasting this long should be evaluated 
by a doctor.

Common causes include:
• Respiratory infections (most common)
• Bronchitis or asthma
• Allergies or post-nasal drip
• In smokers: More serious lung conditions

I recommend:
1. Schedule an appointment with your doctor
2. Monitor for: fever, chest pain, blood in mucus
3. Note any triggers (time of day, activities)

This is for educational purposes only. Please consult a healthcare 
professional for proper diagnosis.

Would you like information about what to expect during a doctor's visit?
```
✅ Empathetic, detailed, conversational, safe

---

## 🛡️ Security & Privacy

### API Key Protection
I'll create `.gitignore` to prevent exposing your key:
```
.env
*.pyc
__pycache__/
```

### Key Storage
```env
# .env file (never committed to git)
GEMINI_API_KEY=your_key_here
# OR
OPENAI_API_KEY=your_key_here
# OR
HUGGINGFACE_API_KEY=your_key_here
```

---

## 💰 Cost Estimation

### Google Gemini (Free Tier)
- **Free**: 60 requests/minute
- **Typical chat**: 500 tokens
- **Can handle**: 3,600 chats/hour FREE
- **Paid**: ~$0.0005 per chat (if exceeded)

### OpenAI GPT-3.5
- **Cost**: ~$0.002 per chat
- **Monthly budget**: $10 = ~5,000 chats

### Hugging Face
- **Free**: Limited requests
- **Pro**: $9/month unlimited

---

## ⚡ Quick Decision Guide

**Choose Gemini if:**
- ✅ You want free tier
- ✅ Don't have credit card
- ✅ Need good quality

**Choose OpenAI if:**
- ✅ Want best quality
- ✅ Have budget ($10-20/month)
- ✅ Need advanced reasoning

**Choose Hugging Face if:**
- ✅ Want open source
- ✅ Need medical-specific models
- ✅ Privacy is priority

---

## 🎬 Next Steps

**Reply with ONE of these:**

**Option 1:** "Use Gemini" (I'll guide you to get key)

**Option 2:** "Use Gemini, my key: AIzaSy..." (I'll implement now)

**Option 3:** "Use OpenAI, my key: sk-..." (I'll implement now)

**Option 4:** "Show me how to get Gemini key" (I'll give detailed steps)

**Option 5:** "Keep current local model" (We'll improve existing ML)

---

## 📚 Below: Technical Details for Local ML Improvements

(Original content for local ML implementation follows...)

---

## Overview
This document outlines the comprehensive AI/ML requirements needed to transform the current keyword-based placeholder into a production-ready disease prediction system.

---

## 1. Natural Language Processing (NLP)

### Required Libraries
```python
spacy>=3.7.0
transformers>=4.35.0
torch>=2.0.0  # For PyTorch-based models
scikit-learn>=1.3.0
nltk>=3.8.1
```

### NLP Tasks
- **Text Preprocessing**: Tokenization, lemmatization, stop word removal
- **Named Entity Recognition (NER)**: Extract symptoms, body parts, severity indicators
- **Intent Classification**: Understand user's primary concern
- **Symptom Extraction**: Identify medical symptoms from free-form text

### Implementation Steps
```python
import spacy
from transformers import pipeline

# Load medical NLP model
nlp = spacy.load("en_core_sci_md")  # SciBERT medical model

# Symptom extraction
def extract_symptoms(text):
    doc = nlp(text)
    symptoms = [ent.text for ent in doc.ents if ent.label_ in ['SYMPTOM', 'DISEASE']]
    return symptoms
```

### Recommended Models
- **BioBERT**: Pre-trained on biomedical literature
- **ClinicalBERT**: Trained on clinical notes
- **SciBERT**: Scientific domain adaptation
- **Custom fine-tuned BERT**: Train on medical Q&A datasets

---

## 2. Disease Prediction Model

### Machine Learning Approach

#### Option A: Classification Model (Recommended for Start)
```python
from sklearn.ensemble import RandomForestClassifier
from sklearn.feature_extraction.text import TfidfVectorizer

# Features: Symptoms (bag-of-words or TF-IDF)
# Labels: Disease categories

model = RandomForestClassifier(n_estimators=200, max_depth=10)
vectorizer = TfidfVectorizer(max_features=500)
```

**Alternatives**:
- XGBoost for better accuracy
- LightGBM for faster training
- Neural Networks for complex patterns

#### Option B: Deep Learning (Production-Grade)
```python
import torch
import torch.nn as nn

class DiseasePredictionModel(nn.Module):
    def __init__(self, input_dim, hidden_dim, num_diseases):
        super().__init__()
        self.encoder = nn.LSTM(input_dim, hidden_dim, batch_first=True)
        self.classifier = nn.Linear(hidden_dim, num_diseases)
    
    def forward(self, symptoms):
        _, (hidden, _) = self.encoder(symptoms)
        return self.classifier(hidden[-1])
```

### Training Data Requirements

**Minimum Dataset Size**: 10,000+ symptom-disease pairs

**Data Sources**:
1. **Medical Datasets** (Public):
   - [Kaggle Disease-Symptom Dataset](https://www.kaggle.com/datasets)
   - NIH Clinical Trials Data
   - CDC Disease Database
   - PubMed Medical Literature

2. **Structured Format**:
```json
{
  "symptoms": ["headache", "fever", "nausea", "fatigue"],
  "disease": "influenza",
  "severity": "moderate",
  "age_group": "adult",
  "gender": "any"
}
```

3. **Cancer-Specific Data**:
   - Breast cancer symptom patterns
   - Lung cancer indicators
   - Colorectal cancer warning signs
   - Prostate cancer symptoms
   - Early detection markers

### Feature Engineering
```python
features = {
    'symptom_count': len(symptoms),
    'severity_score': calculate_severity(symptoms),
    'duration': extract_duration(text),
    'body_systems': identify_affected_systems(symptoms),
    'demographic': {'age': age, 'gender': gender}
}
```

---

## 3. Knowledge Base & Database

### Disease Information Database
```python
# MongoDB schema for diseases
{
    "_id": "disease_001",
    "name": "Influenza",
    "category": "viral_infection",
    "symptoms": [
        {"name": "fever", "weight": 0.9, "critical": false},
        {"name": "cough", "weight": 0.8, "critical": false},
        {"name": "fatigue", "weight": 0.7, "critical": false}
    ],
    "treatments": [
        {
            "type": "medication",
            "name": "Oseltamivir (Tamiflu)",
            "dosage": "75mg twice daily for 5 days",
            "prescription_required": true
        },
        {
            "type": "home_care",
            "description": "Rest, hydration, fever management"
        }
    ],
    "severity_classification": {
        "mild": {"criteria": "low fever, minimal symptoms"},
        "moderate": {"criteria": "high fever, multiple symptoms"},
        "severe": {"criteria": "breathing difficulty, chest pain"}
    },
    "specialist_type": "General Practitioner or Infectious Disease",
    "when_to_seek_emergency": [
        "Difficulty breathing",
        "Chest pain",
        "Confusion",
        "Persistent fever >3 days"
    ]
}
```

### Medicine Database
```python
{
    "medicine_id": "med_001",
    "name": "Acetaminophen",
    "brand_names": ["Tylenol", "Paracetamol"],
    "indications": ["pain", "fever"],
    "dosage": {
        "adult": "500-1000mg every 4-6 hours",
        "child": "10-15mg/kg every 4-6 hours"
    },
    "contraindications": ["liver disease", "alcohol use"],
    "side_effects": ["rare: liver damage", "allergic reaction"],
    "otc_or_prescription": "OTC"
}
```

### Doctor/Hospital Database
```python
{
    "doctor_id": "doc_001",
    "name": "Dr. Sarah Johnson",
    "specialty": "Oncology",
    "sub_specialty": "Breast Cancer",
    "hospital": "City Medical Center",
    "location": {
        "lat": 40.7128,
        "lon": -74.0060,
        "address": "123 Medical Blvd, New York, NY"
    },
    "rating": 4.8,
    "experience_years": 15,
    "accepting_patients": true,
    "insurance_accepted": ["Medicare", "Blue Cross", "Aetna"]
}
```

---

## 4. Critical Condition Detection

### Rule-Based System
```python
CRITICAL_SYMPTOMS = {
    'cardiac': ['chest pain', 'shortness of breath', 'arm pain', 'jaw pain'],
    'neurological': ['sudden confusion', 'slurred speech', 'severe headache'],
    'respiratory': ['inability to breathe', 'blue lips', 'choking'],
    'trauma': ['severe bleeding', 'loss of consciousness', 'broken bones']
}

def detect_critical_condition(symptoms):
    for category, critical_symptoms in CRITICAL_SYMPTOMS.items():
        if any(symptom in symptoms for symptom in critical_symptoms):
            return {
                'is_critical': True,
                'category': category,
                'action': 'CALL 911 IMMEDIATELY'
            }
    return {'is_critical': False}
```

### ML-Based Severity Scoring
```python
from sklearn.ensemble import GradientBoostingRegressor

# Train on labeled severity data (0-10 scale)
severity_model = GradientBoostingRegressor()
severity_model.fit(symptom_features, severity_labels)

# Predict severity for new symptoms
severity_score = severity_model.predict(new_symptoms)
if severity_score > 7:
    recommend_emergency_care()
```

---

## 5. Conversational AI (Optional Advanced Feature)

### Chatbot Framework Options

#### Option A: Rasa (Open Source)
```yaml
# Rasa NLU training data
- intent: report_symptoms
  examples: |
    - I have a headache and fever
    - feeling nauseous and dizzy
    - chest pain for 2 hours

# Rasa dialogue management
stories:
- story: symptom_collection
  steps:
  - intent: report_symptoms
  - action: extract_symptoms
  - action: ask_clarifying_questions
  - action: predict_disease
  - action: recommend_treatment
```

**Cost**: Free (self-hosted)
**Pros**: Full control, privacy, customizable
**Cons**: Requires server maintenance

#### Option B: OpenAI GPT-4 API
```python
import openai

def chat_with_patient(symptoms):
    response = openai.ChatCompletion.create(
        model="gpt-4",
        messages=[
            {"role": "system", "content": "You are a medical assistant helping to understand patient symptoms."},
            {"role": "user", "content": f"I have these symptoms: {symptoms}"}
        ]
    )
    return response.choices[0].message.content
```

**Cost**: ~$0.03 per 1K tokens (input), $0.06 per 1K tokens (output)
**Estimated**: $50-200/month for moderate usage
**Pros**: State-of-the-art NLP, easy integration
**Cons**: Ongoing costs, data privacy concerns

#### Option C: Google Dialogflow
**Cost**: Free tier (180 requests/min), then $0.002/request
**Pros**: Good documentation, integrations
**Cons**: Limited customization

---

## 6. Implementation Roadmap

### Phase 1: MVP (2-4 weeks)
- [ ] Collect 1,000 symptom-disease pairs
- [ ] Train basic classification model (scikit-learn)
- [ ] Implement keyword-based NLP
- [ ] Create disease knowledge base (100 common diseases)
- [ ] Add critical symptom detection
- [ ] Test with 50 real-world scenarios

### Phase 2: Enhanced (4-8 weeks)
- [ ] Expand dataset to 10,000+ examples
- [ ] Fine-tune BERT model for medical text
- [ ] Add medicine database (500 common medicines)
- [ ] Integrate doctor/hospital database
- [ ] Implement severity scoring
- [ ] Add treatment recommendations
- [ ] User feedback loop

### Phase 3: Production (8-12 weeks)
- [ ] Deploy deep learning model
- [ ] Add conversational AI (Rasa or GPT-4)
- [ ] Implement geolocation for hospitals
- [ ] Add appointment scheduling
- [ ] HIPAA compliance (if storing health data)
- [ ] Multi-language support
- [ ] Mobile app integration

---

## 7. Infrastructure Requirements

### Compute Resources
- **Development**: 8GB RAM, 4 CPU cores
- **Training**: 16GB RAM, GPU (NVIDIA T4 or better)
- **Production**: Load-balanced servers, 2-4 instances

### Storage
- **Database**: PostgreSQL or MongoDB (50GB initial)
- **Model Storage**: 2-5GB for trained models
- **Logs**: 10GB/month

### APIs & Services
1. **Geolocation**: Google Maps API ($5-50/month)
2. **NLP**: Hugging Face API (free tier or $9/month)
3. **Conversational AI**: OpenAI API ($50-200/month) OR Rasa (self-hosted)
4. **Email/SMS**: Twilio ($20-100/month)

---

## 8. Cost Estimates

### One-Time Costs
- Dataset acquisition/labeling: $500-2,000
- Model development: 100-200 hours ($5,000-20,000 if outsourced)
- Initial setup: $1,000-3,000

### Monthly Recurring Costs
| Service | Cost |
|---------|------|
| Cloud hosting (AWS/GCP) | $50-150 |
| Database | $20-50 |
| APIs (Maps, NLP, etc.) | $50-200 |
| Conversational AI | $0-200 |
| **Total** | **$120-600/month** |

### Budget-Friendly Approach
- Use free-tier services (Hugging Face, Google Cloud free tier)
- Self-host Rasa instead of using commercial chatbots
- Start with smaller dataset and scale up
- **Estimated**: $20-50/month initial

---

## 9. Accuracy & Validation

### Target Metrics
- **Disease Prediction Accuracy**: 80%+ for common diseases
- **Critical Condition Detection**: 95%+ recall (minimize false negatives)
- **User Satisfaction**: 4.0+ stars
- **Response Time**: <2 seconds

### Testing Strategy
1. **Unit Tests**: Test each component independently
2. **Integration Tests**: End-to-end symptom → treatment flow
3. **Medical Validation**: Review by licensed physicians
4. **User Testing**: Beta with 100+ users

---

## 10. Legal & Compliance

### Disclaimers Required
```
⚠️ IMPORTANT MEDICAL DISCLAIMER:
This chatbot provides general health information only and is not a substitute 
for professional medical advice, diagnosis, or treatment. Always seek the 
advice of your physician or other qualified health provider with any questions 
you may have regarding a medical condition. Never disregard professional 
medical advice or delay in seeking it because of something you have read here.

In case of a medical emergency, call 911 immediately.
```

### Compliance Considerations
- **HIPAA**: If storing patient data (requires encryption, access controls)
- **FDA Regulations**: Medical device classification (consult legal advisor)
- **Data Privacy**: GDPR (EU), CCPA (California)
- **Medical Malpractice Insurance**: Recommended

---

## 11. Next Steps

### Immediate Actions
1. **Acquire training data**: Start with Kaggle datasets
2. **Set up development environment**: Install Python, spaCy, scikit-learn
3. **Build prototype**: 10 diseases, 50 symptoms
4. **Test with stakeholders**: Get feedback from doctors/users
5. **Iterate**: Improve based on feedback

### Recommended Resources
- **Course**: "Clinical Natural Language Processing" (Coursera)
- **Book**: "Deep Medicine" by Eric Topol
- **Dataset**: [Disease-Symptom Knowledge Database](https://people.dbmi.columbia.edu/~friedma/Projects/DiseaseSymptomKB/)
- **Model**: BioBERT from Hugging Face
- **Community**: r/HealthTech, r/MachineLearning

---

## Questions? Contact Information
For technical implementation support or medical domain expertise consultation, 
consider reaching out to:
- Healthcare AI consultants
- Medical informatics specialists
- ML engineers with healthcare experience

**Estimated timeline**: 3-6 months for production-ready system with iterative development.
