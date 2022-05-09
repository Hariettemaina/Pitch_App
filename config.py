import os

from dotenv import load_dotenv, find_dotenv


load_dotenv(find_dotenv())

class Config:
    '''
    General configuration parent class
    '''
   
    MAIL_SERVER = 'smtp.googlemail.com'
    MAIL_PORT = 587
    MAIL_USE_TLS = True
    MAIL_USERNAME = os.environ.get("MAIL_USERNAME")
    MAIL_PASSWORD = os.environ.get("MAIL_PASSWORD")
    
    UPLOADED_PHOTOS_DEST ='app/static/photos'
    
class ProductionConfig(Config):
    
    pass
    
class DevelopmentConfig(Config):
    '''
    '''
    SQLALCHEMY_DATABASE_URI=os.getenv('SQLALCHEMY_DATABASE_URI')
    DEBUG=True
    
    
config_options={
    'dev': DevelopmentConfig,
    'prod': ProductionConfig
}