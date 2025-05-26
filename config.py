import os


class Config:
    SECRET_KEY = 'sua-chave-secreta'
    SQLALCHEMY_DATABASE_URI = 'sqlite:///clubes.db'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
