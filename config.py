import os

class Config:
    '''
    Configuration parent class
    '''
   
class ProdConfig(Config):
    '''
    Production configuration child class
    '''
    pass

class DevConfig(Config):
    '''
    Developement configuration child class
    '''
    pass

    DEBUG = True

config_options = {
'development':DevConfig,
'production':ProdConfig
}