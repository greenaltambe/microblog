import os

class Config:
  SECRET_KEY = os.environ.get('SECRET_KEY') or 'a-hidden-secret-key'