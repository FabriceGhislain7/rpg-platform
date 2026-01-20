import './Navbar.css'

function Navbar({ isAuthenticated = false, user = null, currentPath = '/' }) {
  const nome = user?.nome || 'Utente'
  const crediti = user?.crediti ?? 0

  const isActive = (path) => (currentPath === path ? 'active' : '')

  return (
    <nav className="navbar navbar-expand-lg fixed-top mb-4 fantasy-navbar">
      <div className="container-fluid">
        <a className="navbar-brand fantasy-brand ms-2" href="/">
          <i className="bi bi-shield-fill brand-icon"></i>
          <span className="brand-text">GDR Web</span>
          <div className="brand-glow"></div>
        </a>

        <button
          className="navbar-toggler fantasy-toggler"
          type="button"
          data-bs-toggle="collapse"
          data-bs-target="#navbarNav"
          aria-controls="navbarNav"
          aria-expanded="false"
          aria-label="Toggle navigation"
        >
          <span className="toggler-line"></span>
          <span className="toggler-line"></span>
          <span className="toggler-line"></span>
        </button>

        <div className="collapse navbar-collapse" id="navbarNav">
          <ul className="navbar-nav me-auto">
            <li className="nav-item">
              <a className={`nav-link fantasy-nav-link ${isActive('/')}`} href="/">
                <i className="bi bi-house-door me-1"></i>Home
              </a>
            </li>
            <li className="nav-item">
              <a className={`nav-link fantasy-nav-link ${isActive('/about')}`} href="/about">
                <i className="bi bi-info-circle me-1"></i>About
              </a>
            </li>
            <li className="nav-item">
              <a className={`nav-link fantasy-nav-link ${isActive('/guide')}`} href="/guide">
                <i className="bi bi-book me-1"></i>Game Guide
              </a>
            </li>
            <li className="nav-item">
              <a className={`nav-link fantasy-nav-link ${isActive('/menu')}`} href="/menu">
                <i className="bi bi-controller me-1"></i>Menu Principale
              </a>
            </li>
          </ul>
        </div>

        <div className="d-flex align-items-center ms-auto user-section">
          {isAuthenticated ? (
            <>
              <div className="user-info me-3">
                <span className="user-welcome">
                  <i className="bi bi-person-circle me-1"></i>
                  <span className="user-name">{nome}</span>
                </span>
                <div className="credits-display">
                  <i className="bi bi-coin text-warning me-1"></i>
                  <span className="credits-amount">{crediti}</span>
                  <span className="credits-label">crediti</span>
                </div>
              </div>

              <div className="dropdown">
                <button
                  className="btn fantasy-btn dropdown-toggle"
                  type="button"
                  data-bs-toggle="dropdown"
                  aria-expanded="false"
                >
                  <i className="bi bi-gear"></i>
                </button>
                <ul className="dropdown-menu dropdown-menu-end fantasy-dropdown">
                  <li>
                    <a className="dropdown-item fantasy-dropdown-item" href="/profile">
                      <i className="bi bi-pencil-square me-2"></i>Modifica Profilo
                    </a>
                  </li>
                  <li>
                    <a className="dropdown-item fantasy-dropdown-item" href="/credits">
                      <i className="bi bi-bank me-2"></i>Ricarica Crediti
                    </a>
                  </li>
                  <li><hr className="dropdown-divider" /></li>
                  <li>
                    <a className="dropdown-item fantasy-dropdown-item text-danger" href="/logout">
                      <i className="bi bi-box-arrow-right me-2"></i>Logout
                    </a>
                  </li>
                </ul>
              </div>
            </>
          ) : (
            <div className="auth-buttons">
              <a href="/login" className="btn fantasy-btn-outline me-2">
                <i className="bi bi-box-arrow-in-right me-1"></i>Login
              </a>
              <a href="/register" className="btn fantasy-btn-solid">
                <i className="bi bi-person-plus me-1"></i>Sign up
              </a>
            </div>
          )}
        </div>
      </div>
    </nav>
  )
}

export default Navbar
