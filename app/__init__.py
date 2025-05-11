from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow
from config import config_by_name
import time
import os

db = SQLAlchemy()
ma = Marshmallow()

def create_app(config_name='production'):
    app = Flask(__name__)
    
    # Use environment variable if available, otherwise use the provided config name
    config_env = os.environ.get('FLASK_CONFIG', config_name)
    app.config.from_object(config_by_name[config_env])

    db.init_app(app)
    ma.init_app(app)
    
    # Try to create tables during app initialization
    with app.app_context():
        try:
            db.create_all()
            print("Database tables created on app startup")
        except Exception as e:
            print(f"Warning: Could not create tables on startup: {e}")

    # Import blueprints after initializing the app
    from app.routes.blacklist_routes import blacklist_bp
    app.register_blueprint(blacklist_bp)

    return app
