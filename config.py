import os

class Config:
    DEBUG = os.getenv("DEBUG", False)
    TESTING = os.getenv("TESTING", False)
    SECRET_KEY = os.getenv("SECRET_KEY", "default-secret-key")