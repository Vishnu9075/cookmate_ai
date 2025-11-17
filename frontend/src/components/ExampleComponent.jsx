import { useState } from 'react'

function ExampleComponent({ title, description }) {
  const [isExpanded, setIsExpanded] = useState(false)

  return (
    <div className="example-component">
      <div className="component-header">
        <h3>{title || 'Example Component'}</h3>
        <button 
          onClick={() => setIsExpanded(!isExpanded)}
          className="toggle-button"
        >
          {isExpanded ? 'Collapse' : 'Expand'}
        </button>
      </div>
      
      {isExpanded && (
        <div className="component-content">
          <p>{description || 'This is a reusable React component that can be used throughout the application.'}</p>
          <ul>
            <li>Demonstrates component composition</li>
            <li>Shows state management with useState</li>
            <li>Accepts props for customization</li>
            <li>Provides interactive UI elements</li>
          </ul>
        </div>
      )}
    </div>
  )
}

export default ExampleComponent
