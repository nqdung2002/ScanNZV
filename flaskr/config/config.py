import os
from dotenv import load_dotenv; load_dotenv()

class Config:
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'you-will-never-guess'
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL')
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    TEMPLATE_AUTO_RELOAD = True
    
    # Set up mail server
    MAIL_USERNAME = os.getenv("MAIL_USERNAME")
    MAIL_PASSWORD = os.getenv("MAIL_PASSWORD")
    MAIL_SERVER   = os.getenv("MAIL_SERVER", "smtp.gmail.com")
    MAIL_PORT     = int(os.getenv("MAIL_PORT", "587"))
    MAIL_USE_TLS  = os.getenv("MAIL_USE_TLS", "true").lower() == "true"
    MAIL_USE_SSL = False
    MAIL_DEFAULT_SENDER = ('ScanNZV', MAIL_USERNAME)