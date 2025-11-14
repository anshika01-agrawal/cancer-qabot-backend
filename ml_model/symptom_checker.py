"""
Symptom Checker - Disease Prediction from Symptoms
"""

import os
import json
import joblib
import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.naive_bayes import MultinomialNB
from sklearn.model_selection import train_test_split

class SymptomChecker:
    def __init__(self):
        self.vectorizer = None
        self.model = None
        self.disease_info = {}
        self.models_dir = 'models'
        self.data_dir = 'data'
        
    def load_disease_info(self):
        """Load disease information from JSON"""
        diseases_path = os.path.join(self.data_dir, 'diseases.json')
        if os.path.exists(diseases_path):
            with open(diseases_path, 'r') as f:
                self.disease_info = json.load(f)
    
    def load_models(self):
        """Load trained models from disk"""
        try:
            vectorizer_path = os.path.join(self.models_dir, 'vectorizer.pkl')
            model_path = os.path.join(self.models_dir, 'disease_classifier.pkl')
            
            if os.path.exists(vectorizer_path) and os.path.exists(model_path):
                self.vectorizer = joblib.load(vectorizer_path)
                self.model = joblib.load(model_path)
                self.load_disease_info()
                print("✅ Models loaded successfully")
                return True
            else:
                print("⚠️ No trained models found. Please run train_model.py first")
                return False
        except Exception as e:
            print(f"❌ Error loading models: {e}")
            return False
    
    def train(self, df):
        """Train the disease prediction model"""
        print("Training symptom checker...")
        
        # Initialize vectorizer and model
        self.vectorizer = TfidfVectorizer(
            max_features=500,
            ngram_range=(1, 2),
            stop_words='english'
        )
        self.model = MultinomialNB()
        
        # Prepare data
        X = self.vectorizer.fit_transform(df['symptoms'])
        y = df['disease']
        
        # Split data
        X_train, X_test, y_train, y_test = train_test_split(
            X, y, test_size=0.2, random_state=42
        )
        
        # Train
        self.model.fit(X_train, y_train)
        
        # Evaluate
        accuracy = self.model.score(X_test, y_test)
        print(f"Model accuracy: {accuracy:.2%}")
        
        # Save models
        os.makedirs(self.models_dir, exist_ok=True)
        joblib.dump(self.vectorizer, os.path.join(self.models_dir, 'vectorizer.pkl'))
        joblib.dump(self.model, os.path.join(self.models_dir, 'disease_classifier.pkl'))
        
        # Load disease info
        self.load_disease_info()
        
        print("✅ Model trained and saved")
        return accuracy
    
    def predict(self, symptoms_text):
        """Predict disease from symptoms text"""
        if not self.vectorizer or not self.model:
            raise Exception("Models not loaded. Call load_models() first")
        
        # Clean and preprocess
        symptoms_text = symptoms_text.lower().strip()
        
        # Transform input
        X = self.vectorizer.transform([symptoms_text])
        
        # Predict
        disease = self.model.predict(X)[0]
        probabilities = self.model.predict_proba(X)[0]
        confidence = float(probabilities.max())
        
        # Get all predictions with probabilities
        classes = self.model.classes_
        predictions = [(cls, float(prob)) for cls, prob in zip(classes, probabilities)]
        predictions.sort(key=lambda x: x[1], reverse=True)
        
        return {
            'disease': disease,
            'confidence': confidence * 100,  # Convert to percentage
            'top_predictions': predictions[:5],  # Top 5
            'symptoms_analyzed': symptoms_text
        }
    
    def get_disease_info(self, disease_name):
        """Get detailed information about a disease"""
        # Search in disease_info dict
        for key, info in self.disease_info.items():
            if info.get('name', '').lower() == disease_name.lower():
                return info
        
        # Default response if not found
        return {
            'name': disease_name,
            'severity': 'moderate',
            'treatment': 'Please consult a healthcare professional for proper diagnosis and treatment',
            'specialists': ['General Physician'],
            'emergency_action': 'Schedule a consultation with a doctor'
        }
