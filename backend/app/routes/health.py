"""
Health check endpoint for monitoring application status.
"""
from flask import Blueprint, jsonify

health_bp = Blueprint('health', __name__)


@health_bp.route('/health', methods=['GET'])
def health_check():
    """
    Health check endpoint to verify the application is running.
    
    Returns:
        JSON response with health status
    """
    return jsonify({
        'success': True,
        'data': {
            'status': 'healthy',
            'service': 'backend-api'
        },
        'message': 'Service is running',
        'error': None
    }), 200
