from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config.from_object('config.Config')  # Import config settings

db = SQLAlchemy(app)

from views.auth import auth_bp
app.register_blueprint(auth_bp)

with app.app_context():
    db.create_all()  # Create database tables

if __name__ == '__main__':
    app.run(debug=True)
