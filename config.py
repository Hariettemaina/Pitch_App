import os

class Config:
    '''
    General configuration parent class
    '''
    SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://wagithi:12345j@localhost/pitch'

    
class ProductionConfig(Config):
    
    pass
    
class DevelopmentConfig(Config):
    '''
    '''
    DEBUG=True
    
    
config_options={
    'dev': DevelopmentConfig,
    'prod': ProductionConfig
}