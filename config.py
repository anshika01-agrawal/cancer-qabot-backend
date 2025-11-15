"""
Configuration management for API keys and settings
"""
import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

class Config:
    """Application configuration"""
    
    # Google Gemini API (Primary - Free & Working)
    GOOGLE_API_KEY = os.getenv('GOOGLE_API_KEY')
    
    # Hugging Face API (Backup)
    HUGGINGFACE_API_KEY = os.getenv('HUGGINGFACE_API_KEY')
    HUGGINGFACE_MODEL = os.getenv('HUGGINGFACE_MODEL', 'facebook/blenderbot-400M-distill')
    
    # API settings
    MAX_TOKENS = int(os.getenv('MAX_TOKENS', 500))
    TEMPERATURE = float(os.getenv('TEMPERATURE', 0.7))
    
    @classmethod
    def validate(cls):
        """Validate that required config is present"""
        if not cls.GOOGLE_API_KEY and not cls.HUGGINGFACE_API_KEY:
            print(
                "⚠️ No API keys found! "
                "Add GOOGLE_API_KEY to .env file. "
                "Get it from: https://aistudio.google.com/app/apikey"
            )
            return False
        return True

# Validate on import
try:
    if Config.validate():
        print("✓ Configuration loaded successfully")
except Exception as e:
    print(f"⚠ Configuration warning: {e}")
