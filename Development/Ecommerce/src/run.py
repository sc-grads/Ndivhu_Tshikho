import sys
import os

# Ensure the src directory is included in the path
sys.path.insert(0, os.path.abspath(os.path.dirname(__file__)))

from app import app

if __name__ == '__main__':
    app.run(debug=True)
