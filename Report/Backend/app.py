from flask_cors import CORS
from models import create_app

app = create_app()
CORS(app)

if __name__ == '__main__':
    app.run(debug=True)
from flask_cors import CORS
from models import create_app
import logging  # Import logging module

app = create_app()
CORS(app)

# Set up logging
logging.basicConfig(level=logging.DEBUG)

@app.before_first_request
def setup_logging():
    if not app.debug:
        app.logger.addHandler(logging.StreamHandler())
        app.logger.setLevel(logging.INFO)

if __name__ == '__main__':
    app.run(debug=True)
