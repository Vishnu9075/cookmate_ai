# Full-Stack Web Application

A full-stack web application with a Python backend and React frontend.

## Project Structure

```
project-root/
├── backend/          # Python backend application
│   ├── app/          # Application code
│   │   ├── routes/   # API endpoints
│   │   ├── services/ # Business logic
│   │   ├── models/   # Data models
│   │   └── utils/    # Helper functions
│   ├── tests/        # Backend tests
│   ├── requirements.txt
│   ├── .env.example
│   └── README.md
├── frontend/         # React frontend application
│   ├── src/          # Source code
│   │   ├── components/  # Reusable components
│   │   ├── pages/       # Page components
│   │   ├── services/    # API integration
│   │   └── utils/       # Helper functions
│   ├── public/       # Static assets
│   ├── package.json
│   └── README.md
├── .gitignore        # Git ignore rules
└── README.md         # This file
```

## Prerequisites

- Python 3.8 or higher
- Node.js 16 or higher
- npm or yarn

## Quick Start

### 1. Backend Setup

Navigate to the backend directory and set up the Python environment:

```bash
cd backend

# Create virtual environment
python -m venv venv

# Activate virtual environment
# On Windows:
venv\Scripts\activate
# On macOS/Linux:
source venv/bin/activate

# Install dependencies
pip install -r requirements.txt

# Configure environment variables
copy .env.example .env  # Windows
cp .env.example .env    # macOS/Linux
```

Edit the `.env` file with your configuration:
- `FLASK_ENV`: Set to `development` for development mode
- `PORT`: Backend server port (default: 5000)
- `CORS_ORIGINS`: Allowed frontend origins (default: http://localhost:5173)

Start the backend server:
```bash
python app/main.py
```

The backend API will be available at `http://localhost:5000`

### 2. Frontend Setup

Open a new terminal and navigate to the frontend directory:

```bash
cd frontend

# Install dependencies
npm install

# Start development server
npm run dev
```

The frontend will be available at `http://localhost:5173`

## Development

### Running Both Services

For development, you need to run both the backend and frontend servers simultaneously.

**Terminal 1 - Backend:**
```bash
cd backend
source venv/bin/activate  # or venv\Scripts\activate on Windows
python app/main.py
```

**Terminal 2 - Frontend:**
```bash
cd frontend
npm run dev
```

### Available Scripts

#### Backend
- `python app/main.py` - Start the development server with hot reload

#### Frontend
- `npm run dev` - Start the development server
- `npm run build` - Build for production
- `npm run preview` - Preview production build locally
- `npm run lint` - Run ESLint to check code quality

### API Communication

The frontend is configured to proxy API requests to the backend during development. All requests to `/api/*` will be forwarded to `http://localhost:5000`.

Example API call from frontend:
```javascript
// This will be proxied to http://localhost:5000/api/health
fetch('/api/health')
```

### Environment Variables

#### Backend (.env)
```
FLASK_ENV=development
PORT=5000
CORS_ORIGINS=http://localhost:5173
```

#### Frontend
The frontend uses Vite's built-in proxy configuration (see `vite.config.js`). No additional environment variables are required for basic setup.

## Project Features

- **Backend**: Python-based REST API with Flask
  - RESTful API endpoints
  - CORS configuration for cross-origin requests
  - Environment-based configuration
  - Structured error handling
  - Hot reload in development mode

- **Frontend**: Modern React application built with Vite
  - Fast development server with HMR (Hot Module Replacement)
  - Component-based architecture
  - API client with error handling
  - ESLint for code quality
  - Optimized production builds

## Testing

### Backend Tests
```bash
cd backend
source venv/bin/activate  # or venv\Scripts\activate on Windows
pytest
```

### Frontend Tests
```bash
cd frontend
npm test
```

## Building for Production

### Backend
The backend runs directly with Python. For production deployment:
1. Set `FLASK_ENV=production` in your environment
2. Use a production WSGI server like Gunicorn or uWSGI
3. Configure appropriate CORS origins

### Frontend
```bash
cd frontend
npm run build
```

The production-ready files will be in the `frontend/dist` directory.

Preview the production build locally:
```bash
npm run preview
```

## Troubleshooting

### Backend Issues
- **Port already in use**: Change the `PORT` in `.env` file
- **Module not found**: Ensure virtual environment is activated and dependencies are installed
- **CORS errors**: Check `CORS_ORIGINS` in `.env` matches your frontend URL

### Frontend Issues
- **API requests failing**: Ensure backend is running on port 5000
- **Port already in use**: Vite will automatically try the next available port
- **Dependencies issues**: Delete `node_modules` and `package-lock.json`, then run `npm install`

## Additional Documentation

- Backend API documentation: See `backend/README.md`
- Frontend documentation: See `frontend/README.md`

## License

[Your License Here]
