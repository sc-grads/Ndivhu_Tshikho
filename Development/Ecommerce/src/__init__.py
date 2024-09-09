from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from .views.auth import auth_bp
from .models import user

app = Flask(__name__)
app.config.from_object('config.Config')

db = SQLAlchemy(app)

# Register Blueprints
app.register_blueprint(auth_bp, url_prefix='/auth')

# Initialize the database
db.create_all()
