"""
AI Chatbot using Google Gemini API
Provides intelligent, empathetic medical Q&A responses
"""

import google.generativeai as genai
from config import Config

class AIChatbot:
    """
    AI-powered chatbot using Google Gemini
    Specialized for medical queries with empathetic, safe responses
    """
    
    def __init__(self):
        """Initialize Google Gemini client"""
        try:
            if Config.GOOGLE_API_KEY:
                genai.configure(api_key=Config.GOOGLE_API_KEY)
                self.model = genai.GenerativeModel('gemini-2.0-flash')
                self.client = True
                print(f"✓ AI Chatbot initialized with Google Gemini 2.0")
            else:
                print("⚠ Google API key not found")
                self.client = None
        except Exception as e:
            print(f"⚠ AI Chatbot initialization failed: {e}")
            self.client = None
    
    def _create_medical_prompt(self, user_query):
        """
        Create a medical-specific prompt for Gemini with safety guidelines
        """
        system_context = f"""You are a helpful, empathetic medical information assistant. Your role is to provide supportive, educational information about health concerns.

IMPORTANT GUIDELINES:
1. Be warm, empathetic, and reassuring - never alarm the user
2. Provide educational information, NOT medical diagnosis
3. Always recommend consulting healthcare professionals
4. If symptoms sound serious, gently suggest seeing a doctor without scaring them
5. Give practical, helpful advice
6. Be conversational and supportive

User's question: {user_query}

Provide a helpful, empathetic response (2-3 paragraphs):"""
        
        return system_context
    
    def chat(self, user_message, max_tokens=None, temperature=None):
        """
        Get AI response for user message using Google Gemini
        
        Args:
            user_message (str): User's question or message
            max_tokens (int): Maximum response length (not used in Gemini)
            temperature (float): Response creativity (0.0-1.0)
            
        Returns:
            dict: Response with text and metadata
        """
        if not self.client:
            return {
                'response': 'AI service is not available. Using fallback knowledge base.',
                'source': 'error',
                'model': None
            }
        
        try:
            # Create empathetic medical prompt
            prompt = self._create_medical_prompt(user_message)
            
            # Generate response with Gemini
            response = self.model.generate_content(prompt)
            
            # Extract text
            ai_text = response.text
            
            # Add medical disclaimer
            disclaimer = "\n\n💡 *This is educational information only. For proper medical advice, please consult with a qualified healthcare professional.*"
            
            return {
                'response': ai_text.strip() + disclaimer,
                'source': 'gemini',
                'model': 'gemini-pro',
                'disclaimer': disclaimer
            }
            
        except Exception as e:
            print(f"❌ Gemini error: {e}")
            return {
                'response': 'AI temporarily unavailable. Using fallback knowledge base.',
                'source': 'error',
                'model': 'gemini-pro'
            }
    
    def get_quick_response(self, topic):
        """
        Get quick response for common topics
        
        Args:
            topic (str): Topic keyword (e.g., 'symptoms', 'prevention')
            
        Returns:
            dict: Quick response
        """
        quick_topics = {
            'symptoms': 'What are common cancer warning signs?',
            'prevention': 'How can I reduce my cancer risk?',
            'screening': 'What cancer screenings should I get?',
            'treatment': 'What are common cancer treatment options?',
            'nutrition': 'What diet is recommended during cancer treatment?',
            'support': 'Where can I find cancer support resources?'
        }
        
        query = quick_topics.get(topic.lower(), topic)
        return self.chat(query)

# Global instance
_chatbot_instance = None

def get_chatbot():
    """Get or create chatbot singleton"""
    global _chatbot_instance
    if _chatbot_instance is None:
        _chatbot_instance = AIChatbot()
    return _chatbot_instance
