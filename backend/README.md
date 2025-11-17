# Backend API

Python Flask backend for the full-stack application.

## Setup

### 1. Create and activate a virtual environment

```bash
# Windows
python -m venv venv
venv\Scripts\activate

# macOS/Linux
python -m venv venv
source venv/bin/activate
```

### 2. Install dependencies

```bash
pip install -r requirements.txt
```

### 3. Configure environment variables

Copy the example environment file and edit it with your configuration:

```bash
# Windows
copy .env.example .env

# macOS/Linux
cp .env.example .env
```

Edit the `.env` file with your settings (see Environment Variables section below).

## Running the Application

Start the development server:

```bash
python app/main.py
```

The API will be available at `http://localhost:5000`

The development server includes:
- Hot reload on code changes
- Debug mode for detailed error messages
- CORS enabled for frontend communication

## Environment Variables

Create a `.env` file in the backend directory with the following variables:

### Required Variables

- **FLASK_ENV**: Application environment
  - `development` - Enables debug mode and hot reload
  - `production` - Optimized for production deployment
  - Default: `development`

- **PORT**: Port number for the server
  - Default: `5000`
  - Example: `PORT=5000`

- **CORS_ORIGINS**: Comma-separated list of allowed origins for CORS
  - Required for frontend to communicate with backend
  - Default: `http://localhost:5173`
  - Example: `CORS_ORIGINS=http://localhost:5173,http://localhost:3000`

### Example .env file

```env
FLASK_ENV=development
PORT=5000
CORS_ORIGINS=http://localhost:5173
```

### Environment Variable Notes

- Never commit the `.env` file to version control (it's in `.gitignore`)
- Use `.env.example` as a template for required variables
- For production, set `FLASK_ENV=production` and update `CORS_ORIGINS` to your production frontend URL
- The `CORS_ORIGINS` value must match your frontend URL exactly (including protocol and port)

## API Endpoints

### Health Check
- **GET** `/api/health` - Check if the API is running
  - Returns: `{ "status": "healthy", "message": "API is running" }`

## Project Structure

```
backend/
├── app/
│   ├── __init__.py
│   ├── main.py          # Application entry point
│   ├── config.py        # Configuration management
│   ├── models/          # Data models
│   ├── routes/          # API endpoints
│   │   └── health.py    # Health check endpoint
│   ├── services/        # Business logic
│   │   └── example_service.py
│   └── utils/           # Helper functions
│       ├── response.py  # Response formatters
│       └── errors.py    # Error handlers
├── tests/               # Test files
├── requirements.txt     # Python dependencies
├── .env.example         # Example environment variables
└── README.md           # This file
```

## Development

### Adding New Endpoints

1. Create a new route file in `app/routes/`
2. Define your route handlers
3. Register the blueprint in `app/main.py`

Example:
```python
# app/routes/users.py
from flask import Blueprint

users_bp = Blueprint('users', __name__)

@users_bp.route('/api/users', methods=['GET'])
def get_users():
    return {"users": []}
```

### Using Services

Business logic should be in the `services/` directory:
```python
# app/services/user_service.py
def get_all_users():
    # Business logic here
    return []
```

## Testing

Run tests with pytest:

```bash
pytest
```

Run tests with coverage:

```bash
pytest --cov=app
```

## Troubleshooting

### Port Already in Use
If port 5000 is already in use, change the `PORT` in your `.env` file:
```env
PORT=5001
```

### CORS Errors
If you see CORS errors in the browser console:
1. Check that `CORS_ORIGINS` in `.env` matches your frontend URL exactly
2. Ensure the backend server is running
3. Verify the frontend is making requests to the correct backend URL

### Module Not Found
Ensure your virtual environment is activated:
```bash
# Windows
venv\Scripts\activate

# macOS/Linux
source venv/bin/activate
```

Then reinstall dependencies:
```bash
pip install -r requirements.txt
```
