"""
Test Hugging Face AI Chatbot Integration
Run this to test the AI chatbot before integrating with main app
"""
from ml_model.ai_chatbot import AIChatbot
from config import Config

def test_ai_chatbot():
    """Test the AI chatbot with sample queries"""
    
    print("=" * 60)
    print("🤖 Hugging Face AI Chatbot Test")
    print("=" * 60)
    
    # Initialize chatbot
    print("\n[1] Initializing AI Chatbot...")
    try:
        chatbot = AIChatbot()
        if not chatbot.client:
            print("❌ Failed: Check your HUGGINGFACE_API_KEY in .env file")
            print("\nSteps to fix:")
            print("1. Go to: https://huggingface.co/settings/tokens")
            print("2. Create a new token")
            print("3. Create .env file with: HUGGINGFACE_API_KEY=your_token")
            return
        
        print(f"✅ Success! Using model: {chatbot.model}")
        
    except Exception as e:
        print(f"❌ Error: {e}")
        return
    
    # Test queries
    print("\n[2] Testing AI Responses...")
    print("-" * 60)
    
    test_questions = [
        "What are the early warning signs of lung cancer?",
        "How can I reduce my risk of breast cancer?",
        "What should I do if I find a lump in my breast?",
        "Tell me about healthy diet during cancer treatment",
        "What are the side effects of chemotherapy?"
    ]
    
    for i, question in enumerate(test_questions, 1):
        print(f"\n📝 Question {i}: {question}")
        print("-" * 60)
        
        try:
            result = chatbot.chat(question)
            
            print(f"🤖 AI Response ({result['source']}):")
            print(result['response'])
            
            if result['source'] == 'error':
                print("\n⚠️ Note: Error occurred, check API key and quota")
                
        except Exception as e:
            print(f"❌ Error: {e}")
    
    # Test quick responses
    print("\n" + "=" * 60)
    print("[3] Testing Quick Responses...")
    print("-" * 60)
    
    quick_topics = ['symptoms', 'prevention', 'screening']
    
    for topic in quick_topics:
        print(f"\n📌 Topic: {topic}")
        try:
            result = chatbot.get_quick_response(topic)
            print(f"Response: {result['response'][:150]}...")
        except Exception as e:
            print(f"❌ Error: {e}")
    
    print("\n" + "=" * 60)
    print("✅ AI Chatbot Test Complete!")
    print("=" * 60)

if __name__ == "__main__":
    test_ai_chatbot()
