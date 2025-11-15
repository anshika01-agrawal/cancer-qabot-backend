"""
AI Chatbot using Google Gemini API
Provides intelligent, empathetic medical Q&A responses
"""

import google.generativeai as genai
import json
import os
from config import Config

class AIChatbot:
    """
    AI-powered chatbot using Google Gemini
    Specialized for medical queries with empathetic, safe responses
    """
    
    def __init__(self):
        """Initialize Google Gemini client and load doctors database"""
        try:
            if Config.GOOGLE_API_KEY:
                genai.configure(api_key=Config.GOOGLE_API_KEY)
                self.model = genai.GenerativeModel('gemini-2.0-flash')
                self.client = True
                print(f"✓ AI Chatbot initialized with Google Gemini 2.0")
            else:
                print("⚠ Google API key not found")
                self.client = None
            
            # Load doctors database
            self.doctors_db = self._load_doctors()
            
        except Exception as e:
            print(f"⚠ AI Chatbot initialization failed: {e}")
            self.client = None
    
    def _load_doctors(self):
        """Load doctors database from JSON"""
        try:
            doctors_path = os.path.join('data', 'doctors.json')
            if os.path.exists(doctors_path):
                with open(doctors_path, 'r') as f:
                    return json.load(f)
        except Exception as e:
            print(f"⚠ Could not load doctors database: {e}")
        return {}
    
    def _search_doctors(self, query):
        """
        Search for doctors based on location and specialty
        Returns formatted list of doctors with contact details
        """
        query_lower = query.lower()
        
        # Check if user is asking for doctors without specifying location
        doctor_keywords = ['doctor', 'oncologist', 'endocrinologist', 'physician', 'specialist']
        is_doctor_query = any(keyword in query_lower for keyword in doctor_keywords)
        
        # Detect city from query
        city = None
        available_cities = list(self.doctors_db.keys())
        for city_name in available_cities:
            if city_name.lower() in query_lower:
                city = city_name.lower()
                break
        
        # If asking for doctor but no city specified, return location request
        if is_doctor_query and not city:
            cities_list = ', '.join([c.title() for c in available_cities])
            return "location_needed", f"I'd be happy to help you find a doctor! Which city are you looking for? I have doctor information for: {cities_list}"
        
        if not city:
            return None, None
        
        # Detect specialty from query
        specialty_keywords = {
            'oncologist': 'oncologists',
            'cancer': 'oncologists',
            'endocrinologist': 'endocrinologists',
            'diabetes': 'endocrinologists',
            'thyroid': 'endocrinologists',
            'general': 'general_physicians',
            'physician': 'general_physicians'
        }
        
        specialty = None
        for keyword, spec in specialty_keywords.items():
            if keyword in query_lower:
                specialty = spec
                break
        
        # If no specific specialty, return all doctors in city
        if not specialty:
            all_doctors = []
            for spec_category in self.doctors_db.get(city, {}).values():
                all_doctors.extend(spec_category)
            return all_doctors[:5], None  # Top 5 doctors
        
        # Return doctors for specific specialty
        doctors = self.doctors_db.get(city, {}).get(specialty, [])
        return doctors[:3], None  # Top 3 doctors
    
    def _format_doctors(self, doctors):
        """Format doctors list into readable text"""
        if not doctors:
            return "I couldn't find any doctors matching your criteria. Could you try a different city or specialty?"
        
        result = "Here are some recommended doctors:\n\n"
        for i, doc in enumerate(doctors, 1):
            result += f"{i}. Dr. {doc['name']}\n"
            result += f"   Specialty: {doc['specialty']}\n"
            result += f"   Hospital: {doc['hospital']}\n"
            result += f"   Address: {doc['address']}\n"
            result += f"   Phone: {doc['phone']}\n"
            result += f"   Experience: {doc['experience']}\n"
            result += f"   Consultation Fee: ₹{doc['fee']}\n"
            result += f"   Timings: {doc['timings']}\n"
            result += f"   Rating: {'⭐' * int(doc['rating'])} ({doc['rating']}/5)\n\n"
        
        return result
    
    def _create_medical_prompt(self, query):
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

User's question: {query}

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
            dict: Response with AI text, source, and model info
        """
        try:
            # Check for doctor search query first
            doctors, location_message = self._search_doctors(user_message)
            
            # If location is needed, return prompt
            if doctors == "location_needed":
                return {
                    "response": location_message,
                    "source": "chatbot",
                    "model": "location-prompt"
                }
            
            # If doctors found, format and return
            if doctors:
                doctors_info = self._format_doctors(doctors)
                # Ask Gemini to provide context with doctor list
                prompt = f"""The user asked: "{user_message}"

I found these doctors for them:

{doctors_info}

Please provide a brief, friendly introduction to these recommendations (1-2 sentences), then present the doctor information."""
                
                if self.client:
                    response = self.model.generate_content(prompt)
                    return {
                        "response": response.text,
                        "source": "ai",
                        "model": "gemini-doctor-search"
                    }
                else:
                    return {
                        "response": doctors_info,
                        "source": "database",
                        "model": "doctor-search"
                    }
            
            # Regular medical query - use AI
            if not self.client:
                return {
                    "response": "I apologize, but the AI service is currently unavailable. Please try again later or consult with a healthcare professional directly.",
                    "source": "error",
                    "model": None
                }
            
            # Create medical-focused prompt
            prompt = self._create_medical_prompt(user_message)
            
            # Generate response using Gemini
            response = self.model.generate_content(prompt)
            
            # Return formatted response
            return {
                "response": response.text,
                "source": "ai",
                "model": "gemini-pro"
            }
            
        except Exception as e:
            print(f"⚠ AI Chat error: {e}")
            return {
                "response": f"I encountered an issue processing your request. Please try rephrasing your question or consult with a healthcare professional. Error: {str(e)}",
                "source": "error",
                "model": None
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
