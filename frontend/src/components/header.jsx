export default function Header() {
  return (
    <header className="w-full bg-orange-300 shadow-md">
      <div className="container mx-auto px-4">
        <div className="flex items-center justify-between py-4">
          {/* Logo/Brand */}
          <div className="text-3xl font-bold text-white">
            COOKMATE
          </div>

          {/* Navigation */}
          <nav className="hidden md:flex items-center space-x-6">
            <a href="/" className="text-white hover:text-green-100 transition-colors">
              Home
            </a>
            <a href="/recipes" className="text-white hover:text-green-100 transition-colors">
              Recipes
            </a>
            <a href="/about" className="text-white hover:text-green-100 transition-colors">
              About
            </a>
          </nav>

          {/* Actions */}
          <div className="flex items-center space-x-4">
            <button className="hidden md:block px-4 py-2 text-white border border-white rounded hover:bg-white hover:text-green-600 transition-colors">
              Sign In
            </button>
            <button className="px-4 py-2 bg-white text-green-600 rounded font-semibold hover:bg-green-50 transition-colors">
              Get Started
            </button>
            
            {/* Mobile menu button */}
            <button className="md:hidden text-white" aria-label="Menu">
              <svg className="w-6 h-6" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                <path strokeLinecap="round" strokeLinejoin="round" strokeWidth={2} d="M4 6h16M4 12h16M4 18h16" />
              </svg>
            </button>
          </div>
        </div>
      </div>
    </header>
  );
}
