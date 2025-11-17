/**
 * Example Service
 * Demonstrates API integration patterns for making backend requests
 */

import api from './api';

/**
 * Health check service
 * Calls the backend health endpoint to verify API connectivity
 * @returns {Promise<Object>} Health status response
 */
export const checkHealth = async () => {
  try {
    const response = await api.get('/health');
    return response;
  } catch (error) {
    console.error('Health check failed:', error.message);
    throw error;
  }
};

/**
 * Get example data
 * Fetches example data from the backend for demonstration
 * @returns {Promise<Object>} Example data response
 */
export const getExampleData = async () => {
  try {
    const response = await api.get('/example');
    return response;
  } catch (error) {
    console.error('Failed to fetch example data:', error.message);
    throw error;
  }
};

/**
 * Example GET request
 * Fetches a list of items from the backend
 * @returns {Promise<Array>} List of items
 */
export const getItems = async () => {
  try {
    const response = await api.get('/items');
    return response.data || [];
  } catch (error) {
    console.error('Failed to fetch items:', error.message);
    throw error;
  }
};

/**
 * Example GET by ID request
 * Fetches a single item by ID from the backend
 * @param {string|number} id - Item ID
 * @returns {Promise<Object>} Item data
 */
export const getItemById = async (id) => {
  try {
    const response = await api.get(`/items/${id}`);
    return response.data;
  } catch (error) {
    console.error(`Failed to fetch item ${id}:`, error.message);
    throw error;
  }
};

/**
 * Example POST request
 * Creates a new item on the backend
 * @param {Object} itemData - Item data to create
 * @returns {Promise<Object>} Created item data
 */
export const createItem = async (itemData) => {
  try {
    const response = await api.post('/items', itemData);
    return response.data;
  } catch (error) {
    console.error('Failed to create item:', error.message);
    throw error;
  }
};

/**
 * Example PUT request
 * Updates an existing item on the backend
 * @param {string|number} id - Item ID
 * @param {Object} itemData - Updated item data
 * @returns {Promise<Object>} Updated item data
 */
export const updateItem = async (id, itemData) => {
  try {
    const response = await api.put(`/items/${id}`, itemData);
    return response.data;
  } catch (error) {
    console.error(`Failed to update item ${id}:`, error.message);
    throw error;
  }
};

/**
 * Example DELETE request
 * Deletes an item from the backend
 * @param {string|number} id - Item ID
 * @returns {Promise<Object>} Deletion confirmation
 */
export const deleteItem = async (id) => {
  try {
    const response = await api.delete(`/items/${id}`);
    return response;
  } catch (error) {
    console.error(`Failed to delete item ${id}:`, error.message);
    throw error;
  }
};
