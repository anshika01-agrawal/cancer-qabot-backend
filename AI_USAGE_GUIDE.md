# AI/ML Integration Guide

## Overview
This cancer QA bot now includes real AI/ML capabilities powered by scikit-learn for disease prediction and a knowledge base for medical Q&A.

## Features

### 1. **Symptom-Based Disease Prediction**
- Machine learning model trained on cancer symptoms
- Predicts disease with confidence scores
- Provides alternative diagnoses
- Returns treatment recommendations and specialists

### 2. **Medical Knowledge Q&A**
- Knowledge base with 15+ medical topics
- Categories: symptoms, prevention, treatment, diagnosis, lifestyle
- Returns relevant information with related topics

## Setup & Installation

### 1. Install Dependencies
```bash
pip install -r requirements.txt
```

Required packages:
- fastapi==0.104.1
- uvicorn==0.24.0
- scikit-learn==1.3.2
- pandas==2.1.3
- numpy==1.26.2
- joblib==1.3.2

### 2. Train the Model
```bash
python train_model.py
```

This will:
- Load disease data from `data/diseases.json`
- Create 60+ training samples
- Train TF-IDF vectorizer + Naive Bayes classifier
- Save models to `models/` directory
- Test predictions with sample symptoms

Expected output:
```
============================================================
Cancer Symptom Checker - Model Training
============================================================

[1/3] Preparing training data...
✓ Created 60 training samples from 10 diseases

[2/3] Training machine learning model...
✓ Model trained with 83.33% accuracy

[3/3] Testing model predictions...
✓ Training completed successfully!
```

### 3. Start the Server
```bash
uvicorn main:app --reload
```

The server will:
- Load trained ML models on startup
- Load medical knowledge base
- Serve API endpoints at http://localhost:8000

## API Endpoints

### POST /predict
Predict disease from symptoms

**Request:**
```json
{
  "symptoms": "persistent cough and chest pain for 3 weeks"
}
```

**Response:**
```json
{
  "disease": "Lung Cancer",
  "confidence": "28.3%",
  "alternative_diagnoses": [
    {"disease": "Prostate Cancer", "confidence": "15.2%"},
    {"disease": "Breast Cancer", "confidence": "12.1%"}
  ],
  "severity": "critical",
  "treatment": "Treatment depends on stage and may include surgery, chemotherapy, radiation therapy...",
  "specialists": ["Oncologist", "Pulmonologist", "Thoracic Surgeon"],
  "emergency_action": "Seek immediate medical attention if coughing blood or experiencing severe breathing difficulty",
  "disclaimer": "This is an AI-based preliminary assessment. Always consult qualified medical professionals."
}
```

### POST /chat
Get medical information from knowledge base

**Request:**
```json
{
  "query": "What are the early symptoms of lung cancer?"
}
```

**Response:**
```json
{
  "response": "Early symptoms of lung cancer include persistent cough lasting more than 3 weeks, chest pain that worsens with deep breathing...",
  "topic": "Lung Cancer Early Symptoms",
  "category": "symptoms",
  "related_topics": [
    {"topic": "Breast Cancer Self-Examination", "category": "prevention"},
    {"topic": "Cancer Screening Guidelines", "category": "prevention"}
  ],
  "disclaimer": "This information is for educational purposes only. Consult healthcare professionals."
}
```

## Testing the AI Features

### Run Automated Tests
```bash
python test_ai.py
```

This will test:
- 5 different symptom scenarios for /predict
- 5 different medical questions for /chat
- Display results with confidence scores and treatments

### Manual Testing with curl

**Test disease prediction:**
```bash
curl -X POST http://localhost:8000/predict \
  -H "Content-Type: application/json" \
  -d '{"symptoms": "lump in breast and nipple discharge"}'
```

**Test medical Q&A:**
```bash
curl -X POST http://localhost:8000/chat \
  -H "Content-Type: application/json" \
  -d '{"query": "How does chemotherapy work?"}'
```

## Project Structure

```
cancer-qabot-backend/
├── main.py                 # FastAPI app with AI endpoints
├── train_model.py          # Model training script
├── test_ai.py             # Automated test suite
├── requirements.txt        # Python dependencies
├── ml_model/              # ML package
│   ├── __init__.py
│   ├── symptom_checker.py # Disease prediction model
│   └── knowledge_base.py  # Medical Q&A system
├── data/                  # Training data
│   ├── diseases.json      # 10 cancer types with symptoms
│   └── medical_knowledge.json  # 15 Q&A documents
├── models/                # Trained models (generated)
│   ├── vectorizer.pkl
│   └── disease_classifier.pkl
└── static/                # Frontend files
    ├── landing.html
    ├── auth.html
    └── dashboard.html
```

## Data Files

### diseases.json
Contains 10 cancer types:
- Lung Cancer
- Breast Cancer
- Colon Cancer
- Brain Tumor
- Prostate Cancer
- Lymphoma
- Skin Cancer (Melanoma)
- Leukemia
- Pancreatic Cancer
- Ovarian Cancer

Each disease includes:
- Symptoms (5-7 key symptoms)
- Severity level
- Treatment description
- Specialist doctors
- Emergency action instructions

### medical_knowledge.json
Contains 15 medical topics covering:
- Early symptoms and detection
- Prevention strategies
- Treatment options (chemo, radiation, immunotherapy, targeted therapy)
- Screening guidelines
- Nutrition and lifestyle
- Pain management
- Clinical trials
- Survivor wellness

## How It Works

### Disease Prediction Pipeline
1. **Input**: User enters symptoms as natural text
2. **Preprocessing**: Text is cleaned and lowercased
3. **Vectorization**: TF-IDF converts text to numerical features
4. **Prediction**: Naive Bayes classifier predicts disease
5. **Confidence**: Probability scores for all diseases
6. **Enrichment**: Disease info fetched from knowledge base
7. **Output**: Structured response with treatment and specialists

### Knowledge Base Search
1. **Input**: User asks a medical question
2. **Keyword Matching**: Simple text matching (upgradeable to semantic search)
3. **Ranking**: Documents scored by relevance
4. **Top Results**: Best 3 matches returned
5. **Related Topics**: Suggestions for further reading

## Model Performance

Current metrics (on 60 training samples):
- **Accuracy**: 83.33%
- **Training samples**: 60 (6 per disease)
- **Features**: TF-IDF with 500 max features, bigrams
- **Algorithm**: Multinomial Naive Bayes

### Example Predictions
| Symptoms | Predicted Disease | Confidence |
|----------|------------------|------------|
| persistent cough, chest pain | Lung Cancer | 28.3% |
| breast lump, nipple discharge | Breast Cancer | 42.1% |
| headache, vision problems | Brain Tumor | 34.9% |
| blood in stool, abdominal pain | Colon Cancer | 17.8% |

## Future Enhancements

### Immediate Improvements
- [ ] Add more training data (500+ samples)
- [ ] Implement data augmentation
- [ ] Add symptom duration/severity as features
- [ ] Create confidence threshold warnings

### Advanced Features (Optional)
- [ ] Upgrade to transformer models (BERT, BioBERT)
- [ ] Implement semantic search with sentence-transformers
- [ ] Add FAISS vector database for fast similarity search
- [ ] Integrate external medical APIs (PubMed, Clinical Trials)
- [ ] Add multi-language support
- [ ] Implement conversation memory for chatbot
- [ ] Add medical image analysis (skin lesions, X-rays)

## Troubleshooting

### Models not found
```
⚠ Symptom checker not available
Run 'python train_model.py' to train the model first
```
**Solution**: Run `python train_model.py`

### Port already in use
```
ERROR: address already in use
```
**Solution**: Kill existing process
```bash
lsof -ti:8000 | xargs kill -9
uvicorn main:app --reload
```

### Import errors
```
ModuleNotFoundError: No module named 'sklearn'
```
**Solution**: Install dependencies
```bash
pip install -r requirements.txt
```

## Deployment

### Local Development
```bash
uvicorn main:app --reload --host 0.0.0.0 --port 8000
```

### Production (Heroku)
Already configured with `Procfile`:
```
web: uvicorn main:app --host 0.0.0.0 --port $PORT
```

Before deploying:
1. Commit trained models to git (or train on server startup)
2. Ensure requirements.txt is up to date
3. Test with `python test_ai.py`

## Contributing

To add new diseases:
1. Edit `data/diseases.json`
2. Add disease with symptoms, treatment, specialists
3. Run `python train_model.py` to retrain
4. Test with new symptoms

To add knowledge articles:
1. Edit `data/medical_knowledge.json`
2. Add topic, content, category, tags
3. Restart server to reload knowledge base
4. Test with relevant queries

## Disclaimer

**IMPORTANT**: This is an educational AI system. It is NOT a substitute for professional medical advice, diagnosis, or treatment. Always seek the advice of qualified health providers with any questions about medical conditions.

## License

Educational use only. Consult appropriate licensing for medical AI in production.
