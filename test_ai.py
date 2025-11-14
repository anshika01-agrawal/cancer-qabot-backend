"""
Test script for AI/ML endpoints
"""
import requests
import json

BASE_URL = "http://localhost:8000"

def test_predict():
    """Test disease prediction endpoint"""
    print("=" * 60)
    print("Testing /predict endpoint")
    print("=" * 60)
    
    test_cases = [
        "I have persistent cough and chest pain for 3 weeks",
        "Found a lump in my breast with discharge from nipple",
        "Severe headaches and vision problems, dizziness",
        "Blood in stool, abdominal pain and cramping",
        "Extreme fatigue, weight loss without trying, night sweats"
    ]
    
    for symptoms in test_cases:
        print(f"\n📝 Symptoms: {symptoms}")
        
        try:
            response = requests.post(
                f"{BASE_URL}/predict",
                json={"symptoms": symptoms}
            )
            
            if response.status_code == 200:
                result = response.json()
                print(f"✅ Prediction: {result['disease']}")
                print(f"   Confidence: {result['confidence']}")
                print(f"   Severity: {result['severity']}")
                print(f"   Specialists: {', '.join(result['specialists'])}")
                print(f"   Treatment: {result['treatment'][:80]}...")
            else:
                print(f"❌ Error: {response.status_code}")
                print(f"   {response.json()}")
                
        except Exception as e:
            print(f"❌ Exception: {e}")

def test_chat():
    """Test medical Q&A endpoint"""
    print("\n" + "=" * 60)
    print("Testing /chat endpoint")
    print("=" * 60)
    
    questions = [
        "What are the early symptoms of lung cancer?",
        "How can I prevent breast cancer?",
        "What is chemotherapy and what are the side effects?",
        "Tell me about cancer screening guidelines",
        "How does immunotherapy work?"
    ]
    
    for question in questions:
        print(f"\n💬 Question: {question}")
        
        try:
            response = requests.post(
                f"{BASE_URL}/chat",
                json={"query": question}
            )
            
            if response.status_code == 200:
                result = response.json()
                print(f"✅ Topic: {result['topic']}")
                print(f"   Category: {result['category']}")
                print(f"   Answer: {result['response'][:100]}...")
                if result.get('related_topics'):
                    topics = [t['topic'] for t in result['related_topics']]
                    print(f"   Related: {', '.join(topics)}")
            else:
                print(f"❌ Error: {response.status_code}")
                print(f"   {response.json()}")
                
        except Exception as e:
            print(f"❌ Exception: {e}")

def main():
    print("\n🏥 Cancer QA Bot - AI/ML Endpoints Test")
    print("Make sure the server is running: uvicorn main:app --reload")
    print()
    
    try:
        # Check server
        response = requests.get(f"{BASE_URL}/")
        print("✓ Server is running\n")
        
        # Run tests
        test_predict()
        test_chat()
        
        print("\n" + "=" * 60)
        print("✓ All tests completed!")
        print("=" * 60)
        
    except requests.exceptions.ConnectionError:
        print("❌ Server is not running!")
        print("Start the server with: uvicorn main:app --reload")

if __name__ == "__main__":
    main()
