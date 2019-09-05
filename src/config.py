# /src/config.py

import os

class Development(object):
    """
    Development environment configuration
    """
    DEBUG = True
    TESTING = False
    JWT_SECRET_KEY = "hhgaghhgsdhdhdd"
    SQLALCHEMY_DATABASE_URI = "postgresql://postgres:test@127.0.0.1:5432/blogdb"

class Production(object):
    """
    Production environment configurations
    """
    DEBUG = False
    TESTING = False
    SQLALCHEMY_DATABASE_URI = "postgresql://postgres:test@127.0.0.1:5432/blogdb"
    JWT_SECRET_KEY = "hhgaghhgsdhdhdd"

app_config = {
    'development': Development,
    'production': Production,
}