from flask import Flask
from models import db
from controllers import main
from config import Config

app = Flask(__name__)

# Load configuration from config.py
app.config.from_object(Config)

# Initialize the database with the Flask app
db.init_app(app)

# Register the blueprint (for routes in controllers.py)
app.register_blueprint(main)

if __name__ == '__main__':
    app.run(debug=True)
