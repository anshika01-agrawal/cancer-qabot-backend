"""
Configuration management for API keys and settings
"""
import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

class Config:
    """Application configuration"""
    
    # Hugging Face API
    HUGGINGFACE_API_KEY = os.getenv('HUGGINGFACE_API_KEY')
    HUGGINGFACE_MODEL = os.getenv('HUGGINGFACE_MODEL', 'microsoft/BioGPT-Large')
    
    # Alternative models you can use:
    # - 'microsoft/BioGPT-Large' (Medical text generation - RECOMMENDED)
    # - 'dmis-lab/biobert-base-cased-v1.2' (Medical NER and classification)
    # - 'emilyalsentzer/Bio_ClinicalBERT' (Clinical notes understanding)
    # - 'google/flan-t5-large' (General purpose, good for Q&A)
    
    # API settings
    MAX_TOKENS = int(os.getenv('MAX_TOKENS', 500))
    TEMPERATURE = float(os.getenv('TEMPERATURE', 0.7))
    
    @classmethod
    def validate(cls):
        """Validate that required config is present"""
        if not cls.HUGGINGFACE_API_KEY:
            raise ValueError(
                "HUGGINGFACE_API_KEY not found! "
                "Please create .env file with your Hugging Face token. "
                "Get it from: https://huggingface.co/settings/tokens"
            )
        return True

# Validate on import
try:
    Config.validate()
    print("✓ Configuration loaded successfully")
except ValueError as e:
    print(f"⚠ Configuration warning: {e}")
