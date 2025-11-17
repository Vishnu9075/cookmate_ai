import './App.css'
import Home from './pages/Home'

function App() {
  return (
    <div className="app">
      <header className="app-header">
        <h1>CookMate AI</h1>
        <nav>
          <a href="/">Home</a>
        </nav>
      </header>
      <main className="app-main">
        <Home />
      </main>
      <footer className="app-footer">
        <p>&copy; 2024 CookMate AI. Full-stack application.</p>
      </footer>
    </div>
  )
}

export default App
