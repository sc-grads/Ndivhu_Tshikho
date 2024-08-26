import os

class Config:
    # SQLAlchemy connection URI for SQL Server
    # URL-encode the password. The encoded value of @ is %40.
    SQLALCHEMY_DATABASE_URI = 'mssql+pyodbc://user:Issa100%40@DESKTOP-PL72RR2/ECommerceDB?driver=ODBC+Driver+17+for+SQL+Server'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
