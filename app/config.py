import os
import cloudinary


class Config:
    '''
    General configuration parent class
    '''
    SECRET_KEY = 'anykey'
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
    SQLALCHEMY_DATABASE_URI = os.environ.get("DATABASE_URL")
    JWT_SECRET_KEY = os.getenv('JWT_SECRET_KEY')

class DevConfig(Config):
    '''
    Development  configuration child class

    Args:
        Config: The parent configuration class with General configuration settings
    '''
    SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://postgres:g11111111@localhost/blogging'

    DEBUG = True

config_options = {
    'development': DevConfig,
    'production': ProdConfig,
}