"""
Standardized API response formatter utilities.
"""
from flask import jsonify


def success_response(data=None, message='Success', status_code=200):
    """
    Create a standardized success response.
    
    Args:
        data: Response data (dict, list, or any JSON-serializable object)
        message (str): Success message
        status_code (int): HTTP status code
    
    Returns:
        tuple: JSON response and status code
    """
    response = {
        'success': True,
        'data': data,
        'message': message,
        'error': None
    }
    return jsonify(response), status_code


def error_response(message='Error', error_type='Error', details=None, status_code=400):
    """
    Create a standardized error response.
    
    Args:
        message (str): Error message
        error_type (str): Type of error
        details (dict): Additional error details
        status_code (int): HTTP status code
    
    Returns:
        tuple: JSON response and status code
    """
    error_dict = {
        'type': error_type,
        'message': message
    }
    if details:
        error_dict['details'] = details
    
    response = {
        'success': False,
        'data': None,
        'message': message,
        'error': error_dict
    }
    return jsonify(response), status_code


def paginated_response(items, page=1, per_page=10, total=0, message='Success'):
    """
    Create a standardized paginated response.
    
    Args:
        items (list): List of items for current page
        page (int): Current page number
        per_page (int): Items per page
        total (int): Total number of items
        message (str): Success message
    
    Returns:
        tuple: JSON response and status code
    """
    total_pages = (total + per_page - 1) // per_page if per_page > 0 else 0
    
    response = {
        'success': True,
        'data': {
            'items': items,
            'pagination': {
                'page': page,
                'per_page': per_page,
                'total': total,
                'total_pages': total_pages,
                'has_next': page < total_pages,
                'has_prev': page > 1
            }
        },
        'message': message,
        'error': None
    }
    return jsonify(response), 200
