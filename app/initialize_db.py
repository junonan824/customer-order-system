import sys
import os

# Adjust the path to ensure 'app' can be imported
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from app import db, create_app

app = create_app()
with app.app_context():
    db.create_all()