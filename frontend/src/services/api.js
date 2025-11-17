/**
 * API Client Configuration
 * Provides a configured fetch wrapper for making HTTP requests to the backend API
 */

// Base URL for API requests - uses proxy in development
const API_BASE_URL = import.meta.env.VITE_API_BASE_URL || '/api';

/**
 * Custom error class for API errors
 */
class ApiError extends Error {
  constructor(message, status, data) {
    super(message);
    this.name = 'ApiError';
    this.status = status;
    this.data = data;
  }
}

/**
 * Error handler interceptor
 * Processes error responses and throws structured ApiError
 */
const handleError = async (response) => {
  let errorData;
  try {
    errorData = await response.json();
  } catch {
    errorData = { message: 'An unexpected error occurred' };
  }

  const message = errorData.message || errorData.error || `HTTP ${response.status} Error`;
  throw new ApiError(message, response.status, errorData);
};

/**
 * Response handler interceptor
 * Processes successful responses and extracts data
 */
const handleResponse = async (response) => {
  if (!response.ok) {
    return handleError(response);
  }

  // Handle 204 No Content
  if (response.status === 204) {
    return null;
  }

  try {
    const data = await response.json();
    return data;
  } catch {
    return null;
  }
};

/**
 * Main API client object with HTTP methods
 */
const api = {
  /**
   * GET request
   * @param {string} endpoint - API endpoint path
   * @param {Object} options - Additional fetch options
   * @returns {Promise} Response data
   */
  get: async (endpoint, options = {}) => {
    const response = await fetch(`${API_BASE_URL}${endpoint}`, {
      method: 'GET',
      headers: {
        'Content-Type': 'application/json',
        ...options.headers,
      },
      ...options,
    });
    return handleResponse(response);
  },

  /**
   * POST request
   * @param {string} endpoint - API endpoint path
   * @param {Object} data - Request body data
   * @param {Object} options - Additional fetch options
   * @returns {Promise} Response data
   */
  post: async (endpoint, data, options = {}) => {
    const response = await fetch(`${API_BASE_URL}${endpoint}`, {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json',
        ...options.headers,
      },
      body: JSON.stringify(data),
      ...options,
    });
    return handleResponse(response);
  },

  /**
   * PUT request
   * @param {string} endpoint - API endpoint path
   * @param {Object} data - Request body data
   * @param {Object} options - Additional fetch options
   * @returns {Promise} Response data
   */
  put: async (endpoint, data, options = {}) => {
    const response = await fetch(`${API_BASE_URL}${endpoint}`, {
      method: 'PUT',
      headers: {
        'Content-Type': 'application/json',
        ...options.headers,
      },
      body: JSON.stringify(data),
      ...options,
    });
    return handleResponse(response);
  },

  /**
   * PATCH request
   * @param {string} endpoint - API endpoint path
   * @param {Object} data - Request body data
   * @param {Object} options - Additional fetch options
   * @returns {Promise} Response data
   */
  patch: async (endpoint, data, options = {}) => {
    const response = await fetch(`${API_BASE_URL}${endpoint}`, {
      method: 'PATCH',
      headers: {
        'Content-Type': 'application/json',
        ...options.headers,
      },
      body: JSON.stringify(data),
      ...options,
    });
    return handleResponse(response);
  },

  /**
   * DELETE request
   * @param {string} endpoint - API endpoint path
   * @param {Object} options - Additional fetch options
   * @returns {Promise} Response data
   */
  delete: async (endpoint, options = {}) => {
    const response = await fetch(`${API_BASE_URL}${endpoint}`, {
      method: 'DELETE',
      headers: {
        'Content-Type': 'application/json',
        ...options.headers,
      },
      ...options,
    });
    return handleResponse(response);
  },
};

export default api;
export { ApiError };
