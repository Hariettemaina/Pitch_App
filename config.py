import os

from dotenv import load_dotenv, find_dotenv


load_dotenv(find_dotenv())

class Config:
    '''
    General configuration parent class
    '''
  
    

    
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