"""
AI Chatbot using Hugging Face Inference API
Provides intelligent medical Q&A responses
"""

from huggingface_hub import InferenceClient
from config import Config

class AIChatbot:
    """
    AI-powered chatbot using Hugging Face models
    Specialized for medical queries with safety guidelines
    """
    
    def __init__(self):
        """Initialize Hugging Face client"""
        try:
            Config.validate()
            self.client = InferenceClient(token=Config.HUGGINGFACE_API_KEY)
            self.model = Config.HUGGINGFACE_MODEL
            print(f"✓ AI Chatbot initialized with model: {self.model}")
        except Exception as e:
            print(f"⚠ AI Chatbot initialization failed: {e}")
            self.client = None
    
    def _create_medical_prompt(self, user_query):
        """
        Create a medical-specific prompt with safety guidelines
        """
        system_prompt = """You are a helpful medical information assistant for a cancer awareness chatbot. 
Your role is to provide educational information about cancer symptoms, prevention, and general health guidance.

IMPORTANT GUIDELINES:
1. Always emphasize that you provide educational information, not medical diagnosis
2. Recommend consulting healthcare professionals for actual medical advice
3. Be empathetic and supportive in your responses
4. Provide accurate, evidence-based information
5. If asked about specific diagnosis, remind users to see a doctor
6. Include relevant prevention tips and healthy lifestyle recommendations

User Question: {query}

Provide a helpful, informative response (max 300 words):"""
        
        return system_prompt.format(query=user_query)
    
    def chat(self, user_message, max_tokens=None, temperature=None):
        """
        Get AI response for user message
        
        Args:
            user_message (str): User's question or message
            max_tokens (int): Maximum response length
            temperature (float): Response creativity (0.0-1.0)
            
        Returns:
            dict: Response with text and metadata
        """
        if not self.client:
            return {
                'response': 'AI service is not available. Please check configuration.',
                'source': 'error',
                'model': None
            }
        
        try:
            # Prepare prompt
            prompt = self._create_medical_prompt(user_message)
            
            # Set parameters
            max_tokens = max_tokens or Config.MAX_TOKENS
            temperature = temperature or Config.TEMPERATURE
            
            # Call Hugging Face API
            response = self.client.text_generation(
                prompt,
                model=self.model,
                max_new_tokens=max_tokens,
                temperature=temperature,
                return_full_text=False
            )
            
            # Add medical disclaimer
            disclaimer = "\n\n⚠️ Disclaimer: This is educational information only. Always consult qualified healthcare professionals for medical advice, diagnosis, or treatment."
            
            return {
                'response': response.strip() + disclaimer,
                'source': 'huggingface',
                'model': self.model,
                'disclaimer': disclaimer
            }
            
        except Exception as e:
            print(f"❌ AI chat error: {e}")
            
            # Fallback response
            return {
                'response': f"I encountered an error processing your question. Please try rephrasing or contact support. Error: {str(e)}",
                'source': 'error',
                'model': self.model
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
