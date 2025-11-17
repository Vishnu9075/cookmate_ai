# Frontend Application

React frontend built with Vite for the full-stack application.

## Setup

### 1. Install dependencies

```bash
npm install
```

### 2. Start the development server

```bash
npm run dev
```

The application will be available at `http://localhost:5173`

## Available Scripts

### Development

- **`npm run dev`** - Start the development server
  - Runs on `http://localhost:5173` by default
  - Includes Hot Module Replacement (HMR) for instant updates
  - Automatically proxies API requests to backend

### Production

- **`npm run build`** - Build the application for production
  - Output directory: `dist/`
  - Optimized and minified bundle
  - Ready for deployment

- **`npm run preview`** - Preview the production build locally
  - Serves the built files from `dist/`
  - Useful for testing production build before deployment

### Code Quality

- **`npm run lint`** - Run ESLint to check code quality
  - Checks for code style issues
  - Enforces React best practices
  - Reports errors and warnings

## Project Structure

```
frontend/
├── public/              # Static assets
├── src/
│   ├── components/      # Reusable UI components
│   │   └── ExampleComponent.jsx
│   ├── pages/           # Page-level components
│   │   └── Home.jsx
│   ├── services/        # API integration
│   │   ├── api.js       # API client configuration
│   │   └── exampleService.js
│   ├── utils/           # Helper functions
│   ├── App.jsx          # Root component
│   ├── App.css          # Global styles
│   └── main.jsx         # Application entry point
├── index.html           # HTML template
├── vite.config.js       # Vite configuration
├── eslint.config.js     # ESLint configuration
├── package.json         # Dependencies and scripts
└── README.md           # This file
```

## Configuration

### API Proxy

The frontend is configured to proxy API requests to the backend during development. This is configured in `vite.config.js`:

```javascript
server: {
  proxy: {
    '/api': {
      target: 'http://localhost:5000',
      changeOrigin: true
    }
  }
}
```

This means any request to `/api/*` from the frontend will be forwarded to `http://localhost:5000/api/*`.

### Environment Variables

Vite supports environment variables through `.env` files. Create a `.env` file in the frontend directory if you need custom configuration:

```env
# Example environment variables
VITE_API_URL=http://localhost:5000
```

Access environment variables in your code:
```javascript
const apiUrl = import.meta.env.VITE_API_URL;
```

**Note**: Environment variables must be prefixed with `VITE_` to be exposed to the client-side code.

## Development

### Making API Calls

Use the API client in `src/services/api.js`:

```javascript
import api from './services/api';

// GET request
const data = await api.get('/api/endpoint');

// POST request
const result = await api.post('/api/endpoint', { data: 'value' });
```

### Adding New Components

1. Create a new component file in `src/components/`
2. Export the component
3. Import and use it in your pages or other components

Example:
```jsx
// src/components/Button.jsx
export default function Button({ children, onClick }) {
  return (
    <button onClick={onClick}>
      {children}
    </button>
  );
}
```

### Adding New Pages

1. Create a new page component in `src/pages/`
2. Add routing logic in `App.jsx` (if using React Router)

## Building for Production

Build the application:
```bash
npm run build
```

The production-ready files will be in the `dist/` directory. These files can be:
- Served by any static file server
- Deployed to hosting platforms (Vercel, Netlify, etc.)
- Integrated with your backend deployment

Preview the production build locally:
```bash
npm run preview
```

## Technology Stack

- **React 19** - UI library
- **Vite** - Build tool and development server
  - Fast HMR (Hot Module Replacement)
  - Optimized production builds
  - Built-in TypeScript support
- **ESLint** - Code linting and quality checks

## Troubleshooting

### Port Already in Use

If port 5173 is already in use, Vite will automatically try the next available port (5174, 5175, etc.). Check the terminal output for the actual port.

To specify a custom port, modify `vite.config.js`:
```javascript
server: {
  port: 3000
}
```

### API Requests Failing

If API requests are failing:
1. Ensure the backend server is running on `http://localhost:5000`
2. Check the browser console for CORS errors
3. Verify the proxy configuration in `vite.config.js`
4. Check that the backend has CORS enabled for `http://localhost:5173`

### Build Errors

If you encounter build errors:
1. Delete `node_modules` and `package-lock.json`
2. Run `npm install` again
3. Clear Vite cache: `rm -rf node_modules/.vite`

### ESLint Errors

Fix linting issues automatically:
```bash
npm run lint -- --fix
```

## Additional Resources

- [Vite Documentation](https://vitejs.dev/)
- [React Documentation](https://react.dev/)
- [ESLint Documentation](https://eslint.org/)
