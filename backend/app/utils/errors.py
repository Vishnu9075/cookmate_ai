"""
Custom exception classes and error handlers for the application.
"""
from flask import jsonify


class APIError(Exception):
    """Base exception class for API errors."""
    
    def __init__(self, message, status_code=400, payload=None):
        """
        Initialize API error.
        
        Args:
            message (str): Error message
            status_code (int): HTTP status code
            payload (dict): Additional error details
        """
        super().__init__()
        self.message = message
        self.status_code = status_code
        self.payload = payload
    
    def to_dict(self):
        """
        Convert error to dictionary format.
        
        Returns:
            dict: Error details in standardized format
        """
        error_dict = {
            'success': False,
            'data': None,
            'message': self.message,
            'error': {
                'type': self.__class__.__name__,
                'message': self.message
            }
        }
        if self.payload:
            error_dict['error']['details'] = self.payload
        return error_dict


class ValidationError(APIError):
    """Exception for validation errors."""
    
    def __init__(self, message, payload=None):
        super().__init__(message, status_code=400, payload=payload)


class NotFoundError(APIError):
    """Exception for resource not found errors."""
    
    def __init__(self, message, payload=None):
        super().__init__(message, status_code=404, payload=payload)


class UnauthorizedError(APIError):
    """Exception for unauthorized access errors."""
    
    def __init__(self, message, payload=None):
        super().__init__(message, status_code=401, payload=payload)


class ForbiddenError(APIError):
    """Exception for forbidden access errors."""
    
    def __init__(self, message, payload=None):
        super().__init__(message, status_code=403, payload=payload)


class ServerError(APIError):
    """Exception for internal server errors."""
    
    def __init__(self, message, payload=None):
        super().__init__(message, status_code=500, payload=payload)


def register_error_handlers(app):
    """
    Register error handlers with the Flask application.
    
    Args:
        app (Flask): Flask application instance
    """
    
    @app.errorhandler(APIError)
    def handle_api_error(error):
        """Handle custom API errors."""
        response = jsonify(error.to_dict())
        response.status_code = error.status_code
        return response
    
    @app.errorhandler(404)
    def handle_not_found(error):
        """Handle 404 errors."""
        return jsonify({
            'success': False,
            'data': None,
            'message': 'Resource not found',
            'error': {
                'type': 'NotFoundError',
                'message': 'The requested resource was not found'
            }
        }), 404
    
    @app.errorhandler(500)
    def handle_server_error(error):
        """Handle 500 errors."""
        return jsonify({
            'success': False,
            'data': None,
            'message': 'Internal server error',
            'error': {
                'type': 'ServerError',
                'message': 'An unexpected error occurred'
            }
        }), 500
