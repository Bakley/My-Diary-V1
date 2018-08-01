import os

class Config:
    """Parent configuration class"""
    DEBUG = False
    CSRF_ENABLED = True
    SECRET = os.getenv('SECRET')


class DevelopmentConfig(Config):
    """Configurations for Development"""
    DEBUG = True
    ENV = "development"


class TestingConfig(Config):
    """Configurations for Testing, with a separate database."""
    TESTING = True


class ProductionConfig(Config):
    """Configurations for Production."""
    DEBUG = False
    TESTING = False


app_config = {
    'development': DevelopmentConfig,
    'testing': TestingConfig,
    'production': ProductionConfig
}

# This impoted to the app/__init__.py
