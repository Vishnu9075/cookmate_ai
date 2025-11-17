import { useState, useEffect } from 'react'
import ExampleComponent from '../components/ExampleComponent'
import { getExampleData } from '../services/exampleService'

function Home() {
  const [data, setData] = useState(null)
  const [loading, setLoading] = useState(false)
  const [error, setError] = useState(null)

  const handleFetchData = async () => {
    setLoading(true)
    setError(null)
    try {
      const result = await getExampleData()
      setData(result)
    } catch (err) {
      setError(err.message || 'Failed to fetch data')
    } finally {
      setLoading(false)
    }
  }

  return (
    <div className="home-page">
      <h2>Welcome to CookMate AI</h2>
      <p>A full-stack application with Python backend and React frontend.</p>
      
      <ExampleComponent 
        title="API Integration Example"
        description="Click the button below to test the backend API connection"
      />

      <div className="api-test-section">
        <button 
          onClick={handleFetchData} 
          disabled={loading}
          className="fetch-button"
        >
          {loading ? 'Loading...' : 'Fetch Data from Backend'}
        </button>

        {error && (
          <div className="error-message">
            <p>Error: {error}</p>
          </div>
        )}

        {data && (
          <div className="data-display">
            <h3>Response from Backend:</h3>
            <pre>{JSON.stringify(data, null, 2)}</pre>
          </div>
        )}
      </div>
    </div>
  )
}

export default Home
