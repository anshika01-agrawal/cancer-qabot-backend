"""
Training script for cancer symptom checker ML model
"""
import pandas as pd
import json
from ml_model.symptom_checker import SymptomChecker

def prepare_training_data():
    """
    Prepare training data from diseases.json
    """
    # Load diseases data
    with open('data/diseases.json', 'r') as f:
        diseases_dict = json.load(f)
    
    training_data = []
    
    # Create training samples from each disease
    # diseases.json is a dict with disease_key: disease_data structure
    for disease_key, disease in diseases_dict.items():
        disease_name = disease['name']
        symptoms_list = disease['symptoms']
        
        # Create multiple training samples by combining symptoms
        # Full symptom set
        training_data.append({
            'symptoms': ', '.join(symptoms_list),
            'disease': disease_name
        })
        
        # Combinations of symptoms for robustness
        if len(symptoms_list) >= 3:
            # First 3 symptoms
            training_data.append({
                'symptoms': ', '.join(symptoms_list[:3]),
                'disease': disease_name
            })
            # Last 3 symptoms
            training_data.append({
                'symptoms': ', '.join(symptoms_list[-3:]),
                'disease': disease_name
            })
        
        # Individual symptom variations
        for symptom in symptoms_list[:3]:  # Use first 3 to avoid oversampling
            training_data.append({
                'symptoms': symptom,
                'disease': disease_name
            })
    
    return pd.DataFrame(training_data)

def main():
    """
    Main training function
    """
    print("=" * 60)
    print("Cancer Symptom Checker - Model Training")
    print("=" * 60)
    
    # Prepare data
    print("\n[1/3] Preparing training data...")
    df = prepare_training_data()
    print(f"✓ Created {len(df)} training samples from {df['disease'].nunique()} diseases")
    
    # Initialize and train model
    print("\n[2/3] Training machine learning model...")
    checker = SymptomChecker()
    accuracy = checker.train(df)
    print(f"✓ Model trained with {accuracy:.2f}% accuracy")
    
    # Test the model
    print("\n[3/3] Testing model predictions...")
    test_cases = [
        "persistent cough and chest pain",
        "lump in breast and nipple discharge",
        "severe headache and vision problems",
        "blood in stool and abdominal pain",
        "fatigue and unexplained weight loss"
    ]
    
    for test_symptoms in test_cases:
        result = checker.predict(test_symptoms)
        print(f"\nSymptoms: {test_symptoms}")
        print(f"  → Predicted: {result['disease']} ({result['confidence']:.1f}% confidence)")
        top_3_str = ', '.join([f"{d} ({c:.0f}%)" for d, c in result['top_predictions']])
        print(f"  → Top 3: {top_3_str}")
    
    print("\n" + "=" * 60)
    print("✓ Training completed successfully!")
    print("✓ Models saved to: models/vectorizer.pkl and models/disease_classifier.pkl")
    print("=" * 60)

if __name__ == "__main__":
    main()
