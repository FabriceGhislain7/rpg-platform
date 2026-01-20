import { useEffect, useRef, useState } from 'react'
import './Footer.css'

function Footer() {
  const [currentTime, setCurrentTime] = useState('')
  const titleRef = useRef(null)

  useEffect(() => {
    const updateTime = () => {
      const now = new Date()
      setCurrentTime(now.toLocaleTimeString('it-IT', { hour: '2-digit', minute: '2-digit' }))
    }
    updateTime()
    const id = setInterval(updateTime, 60000)
    return () => clearInterval(id)
  }, [])

  const handleTitleClick = () => {
    window.scrollTo({ top: 0, behavior: 'smooth' })
    if (titleRef.current) {
      titleRef.current.style.transform = 'scale(1.1)'
      setTimeout(() => {
        if (titleRef.current) titleRef.current.style.transform = 'scale(1)'
      }, 200)
    }
  }

  return (
    <footer className="footer mt-auto py-4 bg-dark text-light">
      <div className="container">
        <div className="row align-items-center">
          <div className="col-md-6 mb-3 mb-md-0">
            <h5 className="text-warning fw-bold mb-2" ref={titleRef} onClick={handleTitleClick}>
              <i className="bi bi-shield-fill me-2"></i>GDR Web
            </h5>
            <p className="small text-muted mb-0">
              Il tuo portale per avventure fantasy epiche online.
            </p>
          </div>

          <div className="col-md-6 text-md-end">
            <div className="mb-2">
              <span className="text-light-gray small">
                <i className="bi bi-code-slash me-1"></i>Sviluppato da{' '}
                <span className="text-warning fw-semibold">Fabrice Ghislain Tebou</span>
              </span>
            </div>
            <div className="social-links">
              <a
                href="https://www.linkedin.com/in/fabrice-ghislain-tebou-72000b211"
                target="_blank"
                rel="noreferrer"
                className="text-light-gray me-2"
                title="LinkedIn"
                aria-label="LinkedIn"
              >
                <i className="bi bi-linkedin"></i>
              </a>
              <a
                href="mailto:ghislaintebou@gmail.com"
                className="text-light-gray"
                title="Email"
                aria-label="Email"
              >
                <i className="bi bi-envelope-fill"></i>
              </a>
            </div>
          </div>
        </div>

        <hr className="my-3 border-secondary" />

        <div className="row align-items-center">
          <div className="col-md-4">
            <span className="text-light-gray small">
              <i className="bi bi-shield-check me-1"></i>
              Tutti i diritti riservati.
              <a href="/privacy" className="text-light-gray text-decoration-none hover-link"> Privacy Policy</a> |
              <a href="/terms" className="text-light-gray text-decoration-none hover-link"> Termini di Servizio</a>
            </span>
          </div>

          <div className="col-md-4 text-center">
            <span className="text-light-gray small">
              <i className="bi bi-calendar3 me-1"></i>&copy; 2025 GDR Web
            </span>
          </div>

          <div className="col-md-4 text-md-end">
            <span className="text-light-gray small">
              <i className="bi bi-cpu me-1"></i>
              Versione 1.0.0 | <span id="current-time" className="text-warning">{currentTime}</span>
            </span>
          </div>
        </div>
      </div>
    </footer>
  )
}

export default Footer
