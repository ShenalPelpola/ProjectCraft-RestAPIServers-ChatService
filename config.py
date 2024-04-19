import os
from dotenv import load_dotenv

load_dotenv()

class Config(object):
    """Base configuration."""
    DEBUG = False
    Testing = False
    OPENAI_API_KEY = os.getenv('OPENAI_API_KEY')
    REDIS_URL = "redis://localhost:6379"
    CHAT_OPEN_AI = {
        "DEFAULT_MODEL": "gpt-3.5-turbo-0125",
        "DEFAULT_TEMPERATURE": 0
    }

class ProductionConfig(Config):
    """Production specific config."""
    DEBUG = False
    TESTING = False

class DevelopmentConfig(Config):
    """Development environment specific config."""
    DEBUG = True

class TestConfig(Config):
    """Testing environment specific config."""
    TESTING = True