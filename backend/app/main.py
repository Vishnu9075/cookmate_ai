"""
Main application entry point for the Flask backend.
Initializes the Flask app, configures CORS, registers routes, and starts the development server.
"""
import sys
import os

# Add the backend directory to the Python path
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from flask import Flask
from flask_cors import CORS
from app.config import get_config
from app.routes.health import health_bp


def create_app():
    """
    Application factory function to create and configure the Flask app.
    
    Returns:
        Flask: Configured Flask application instance
    """
    app = Flask(__name__)
    
    # Load configuration
    config = get_config()
    app.config.from_object(config)
    
    # Configure CORS
    CORS(app, resources={
        r"/*": {
            "origins": config.CORS_ORIGINS,
            "methods": ["GET", "POST", "PUT", "DELETE", "OPTIONS"],
            "allow_headers": ["Content-Type", "Authorization"]
        }
    })
    
    # Register blueprints
    app.register_blueprint(health_bp, url_prefix=config.API_PREFIX)
    
    return app


def main():
    """
    Main function to run the Flask development server.
    """
    app = create_app()
    config = get_config()
    
    print(f"Starting Flask server on {config.HOST}:{config.PORT}")
    print(f"Environment: {config.ENV}")
    print(f"Debug mode: {config.DEBUG}")
    
    app.run(
        host=config.HOST,
        port=config.PORT,
        debug=config.DEBUG
    )


if __name__ == '__main__':
    main()
