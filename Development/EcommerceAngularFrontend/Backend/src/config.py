import os

class Config:
    # SQLAlchemy connection URI for SQL Server
    # URL-encode the password if it contains special characters.
    SQLALCHEMY_DATABASE_URI = (
        'mssql+pyodbc://user:Issa100%40@DESKTOP-PL72RR2/ECommerceDB?driver=ODBC+Driver+17+for+SQL+Server'
    )
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'your_secret_key'
 