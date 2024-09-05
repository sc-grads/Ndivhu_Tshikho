from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from flask import Flask
from flask_jwt_extended import JWTManager

db = SQLAlchemy()
bcrypt = Bcrypt()
jwt = JWTManager()

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(150), unique=True, nullable=False)
    email = db.Column(db.String(150), unique=True, nullable=False)
    password = db.Column(db.String(256), nullable=False)

    def check_password(self, password):
        return bcrypt.check_password_hash(self.password, password)

def create_app():
    app = Flask(__name__)
    app.config.from_object('config.Config')  # Updated to load config properly
    db.init_app(app)
    bcrypt.init_app(app)
    jwt.init_app(app)

    from routes.auth import auth_blueprint  # Corrected import path
    app.register_blueprint(auth_blueprint, url_prefix='/auth')

    with app.app_context():
        db.create_all()

    return app
