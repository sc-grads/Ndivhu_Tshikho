from flask import Flask
from flask_cors import CORS
from config import Config
from routes import auth

app = Flask(__name__)
app.config.from_object(Config)

# Enable CORS for the whole application
CORS(app, resources={r"/api/*": {"origins": "*"}})

# Register your routes
app.register_blueprint(auth.bp)

if __name__ == '__main__':
    app.run(debug=True)
