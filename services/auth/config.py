import os

class Config:
    SQLALCHEMY_DATABASE_URI = 'postgresql://postgres:postgres@postgres/auth_db'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
