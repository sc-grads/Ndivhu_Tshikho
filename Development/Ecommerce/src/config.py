import os

class Config:
    SQLALCHEMY_DATABASE_URI = 'sqlite:///ecommerce.db'  # SQLite database file
    SQLALCHEMY_TRACK_MODIFICATIONS = False
