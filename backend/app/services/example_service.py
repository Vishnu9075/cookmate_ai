"""
Example service module demonstrating business logic layer.
This module contains sample business logic functions that can be called from route handlers.
"""
from app.utils.errors import ValidationError, NotFoundError


def process_data(input_data):
    """
    Example function that processes input data with validation.
    
    Args:
        input_data (dict): Input data to process
    
    Returns:
        dict: Processed data
    
    Raises:
        ValidationError: If input data is invalid
    """
    if not input_data:
        raise ValidationError('Input data is required')
    
    if not isinstance(input_data, dict):
        raise ValidationError('Input data must be a dictionary')
    
    # Example processing logic
    processed = {
        'original': input_data,
        'processed': True,
        'item_count': len(input_data)
    }
    
    return processed


def get_item_by_id(item_id):
    """
    Example function that retrieves an item by ID.
    
    Args:
        item_id (int): ID of the item to retrieve
    
    Returns:
        dict: Item data
    
    Raises:
        ValidationError: If item_id is invalid
        NotFoundError: If item is not found
    """
    if not item_id or not isinstance(item_id, (int, str)):
        raise ValidationError('Valid item ID is required')
    
    # Example: In a real application, this would query a database
    # For demonstration, we'll use a mock data structure
    mock_items = {
        '1': {'id': 1, 'name': 'Item One', 'description': 'First example item'},
        '2': {'id': 2, 'name': 'Item Two', 'description': 'Second example item'},
        '3': {'id': 3, 'name': 'Item Three', 'description': 'Third example item'}
    }
    
    item = mock_items.get(str(item_id))
    
    if not item:
        raise NotFoundError(f'Item with ID {item_id} not found')
    
    return item


def calculate_statistics(numbers):
    """
    Example function that calculates statistics from a list of numbers.
    
    Args:
        numbers (list): List of numbers
    
    Returns:
        dict: Statistical calculations
    
    Raises:
        ValidationError: If input is invalid
    """
    if not numbers:
        raise ValidationError('Numbers list is required')
    
    if not isinstance(numbers, list):
        raise ValidationError('Input must be a list')
    
    if not all(isinstance(n, (int, float)) for n in numbers):
        raise ValidationError('All items must be numbers')
    
    if len(numbers) == 0:
        raise ValidationError('Numbers list cannot be empty')
    
    # Calculate statistics
    total = sum(numbers)
    count = len(numbers)
    average = total / count
    minimum = min(numbers)
    maximum = max(numbers)
    
    return {
        'count': count,
        'sum': total,
        'average': average,
        'min': minimum,
        'max': maximum
    }
