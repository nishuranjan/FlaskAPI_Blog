# /src/config.py

import os

class Development(object):
    """
    Development environment configuration
    """
    DEBUG = True
    TESTING = False
    JWT_SECRET_KEY = "hhgaghhgsdhdhdd"
    SQLALCHEMY_DATABASE_URI = "postgresql://postgres:post2020APIDB@apidbfordev.clbolncrkftt.us-east-2.rds.amazonaws.com:5432/APIDBFORDEV"
	
class Production(object):
    """
    Production environment configurations
    """
    DEBUG = False
    TESTING = False
    SQLALCHEMY_DATABASE_URI = "postgresql://dnzociatsyinxn:09cd7945be0c0df341c33673920938bacdd9b87733c37b603b4dec02ec4df9b4@ec2-54-163-226-238.compute-1.amazonaws.com:5432/d585c2k4ch7dr0"
    JWT_SECRET_KEY = "hhgaghhgsdhdhdd"

app_config = {
    'development': Development,
    'production': Production,
}