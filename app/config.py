import os
import cloudinary
class Config:
    '''
    General configuration parent class
    '''
SECRET_KEY = 'SECRET_KEY'
SQLALCHEMY_DATABASE_URI = os.environ.get('SQLALCHEMY_DATABASE_URI')
SQLALCHEMY_TRACK_MODIFICATIONS = False
UPLOADED_PHOTOS_DEST = 'app/static/photos'

# cloudinary configuration
cloudinary.config(cloud_name='group6flask', api_key='771748118468722',
                  api_secret='Uye0Bi1UGZRvFNO8O8viekFqqIE')

class ProdConfig(Config):
    '''
    Production  configuration child class

    Args:
        Config: The parent configuration class with General configuration settings
    '''
    pass


class DevConfig(Config):
    '''
    Development  configuration child class

    Args:
        Config: The parent configuration class with General configuration settings
    '''

    DEBUG = True