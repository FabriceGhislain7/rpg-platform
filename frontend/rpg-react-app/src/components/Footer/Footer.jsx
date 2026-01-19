import { useEffect, useRef, useState } from 'react'
import './Footer.css'

function Footer({ isAuthenticated = false }) {
  const [currentTime, setCurrentTime] = useState('')
  const titleRef = useRef(null)

  useEffect(() => {
    const updateTime = () => {
      const now = new Date()
      const timeString = now.toLocaleTimeString('it-IT', {
        hour: '2-digit',
        minute: '2-digit',
      })
      setCurrentTime(timeString)
    }

    updateTime()
    const intervalId = setInterval(updateTime, 60000)

    return () => clearInterval(intervalId)
  }, [])

  const handleTitleClick = () => {
    window.scrollTo({ top: 0, behavior: 'smooth' })
    if (titleRef.current) {
      titleRef.current.style.transform = 'scale(1.1)'
      setTimeout(() => {
        if (titleRef.current) {
          titleRef.current.style.transform = 'scale(1)'
        }
      }, 200)
    }
  }

  const handleSparkle = (e) => {
    const sparkle = document.createElement('div')
    sparkle.innerHTML = '✨'
    sparkle.style.position = 'absolute'
    sparkle.style.left = `${e.pageX}px`
    sparkle.style.top = `${e.pageY}px`
    sparkle.style.pointerEvents = 'none'
    sparkle.style.fontSize = '20px'
    sparkle.style.zIndex = '9999'
    sparkle.style.animation = 'sparkleFloat 1s ease-out forwards'

    document.body.appendChild(sparkle)

    setTimeout(() => {
      sparkle.remove()
    }, 1000)
  }

  return (
    <footer className="footer mt-auto py-4 bg-dark text-light">
      <div className="container">
        <div className="row align-items-center">
          <div className="col-md-4 mb-3 mb-md-0">
            <h5 className="text-warning fw-bold mb-2" ref={titleRef} onClick={handleTitleClick}>
              <i className="bi bi-shield-fill me-2"></i>GDR Web
            </h5>
            <p className="small text-muted mb-0">
              Il tuo portale per avventure fantasy epiche online.
            </p>
          </div>

          <div className="col-md-4 mb-3 mb-md-0">
            <h6 className="text-light fw-semibold mb-2">Link Rapidi</h6>
            <div className="d-flex flex-wrap gap-3">
              <a href="/about" className="text-light-gray text-decoration-none small hover-link">
                <i className="bi bi-info-circle me-1"></i>About
              </a>
              <a href="/guide" className="text-light-gray text-decoration-none small hover-link">
                <i className="bi bi-book me-1"></i>Guida
              </a>
              <a href="/credits" className="text-light-gray text-decoration-none small hover-link">
                <i className="bi bi-heart me-1"></i>Credits
              </a>
              {isAuthenticated ? (
                <a href="/menu" className="text-warning text-decoration-none small hover-link">
                  <i className="bi bi-controller me-1"></i>Menu
                </a>
              ) : (
                <a href="/login" className="text-warning text-decoration-none small hover-link">
                  <i className="bi bi-box-arrow-in-right me-1"></i>Login
                </a>
              )}
            </div>
          </div>

          <div className="col-md-4 text-md-end">
            <div className="mb-2">
              <span className="text-light-gray small">
                <i className="bi bi-calendar3 me-1"></i>&copy; 2025 GDR Web
              </span>
            </div>
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
                title="LinkedIn Profile"
                aria-label="LinkedIn"
                onClick={handleSparkle}
              >
                <i className="bi bi-linkedin"></i>
              </a>
              <a
                href="mailto:ghislaintebou@gmail.com"
                className="text-light-gray me-2"
                title="ghislaintebou@gmail.com"
                aria-label="Email"
                onClick={handleSparkle}
              >
                <i className="bi bi-envelope-fill"></i>
              </a>
              <a
                href="https://github.com/FabriceGhislain7"
                target="_blank"
                rel="noreferrer"
                className="text-light-gray me-2"
                title="GitHub Profile"
                aria-label="GitHub"
                onClick={handleSparkle}
              >
                <i className="bi bi-github"></i>
              </a>
              <a
                href="tel:+393519957025"
                className="text-light-gray"
                title="+39 351 995 7025"
                aria-label="Telefono"
                onClick={handleSparkle}
              >
                <i className="bi bi-telephone-fill"></i>
              </a>
            </div>
          </div>
        </div>

        <hr className="my-3 border-secondary" />

        <div className="row align-items-center">
          <div className="col-md-6">
            <span className="text-light-gray small">
              <i className="bi bi-shield-check me-1"></i>
              Tutti i diritti riservati.
              <a href="#" className="text-light-gray text-decoration-none hover-link"> Privacy Policy</a> |
              <a href="#" className="text-light-gray text-decoration-none hover-link"> Termini di Servizio</a>
            </span>
          </div>
          <div className="col-md-6 text-md-end">
            <span className="text-light-gray small">
              <i className="bi bi-cpu me-1"></i>
              Versione 1.0.0 | <span id="current-time" className="text-warning">{currentTime}</span>
            </span>
          </div>
        </div>

        <div className="row mt-3 d-md-none">
          <div className="col-12 text-center">
            <div className="developer-card p-3 rounded bg-dark border border-secondary">
              <h6 className="text-warning mb-2">
                <i className="bi bi-person-badge me-1"></i>Sviluppatore
              </h6>
              <p className="text-light-gray small mb-2">
                <strong>Fabrice Ghislain Tebou</strong><br />
                Full Stack Developer specializzato in Python/Flask<br />
                <i className="bi bi-envelope me-1"></i>ghislaintebou@gmail.com<br />
                <i className="bi bi-telephone me-1"></i>+39 351 995 7025
              </p>
              <div className="contact-links">
                <a
                  href="https://www.linkedin.com/in/fabrice-ghislain-tebou-72000b211"
                  target="_blank"
                  rel="noreferrer"
                  className="btn btn-outline-warning btn-sm me-2 mb-2"
                  onClick={handleSparkle}
                >
                  <i className="bi bi-linkedin me-1"></i>LinkedIn
                </a>
                <a
                  href="mailto:ghislaintebou@gmail.com"
                  className="btn btn-outline-warning btn-sm me-2 mb-2"
                  onClick={handleSparkle}
                >
                  <i className="bi bi-envelope me-1"></i>Email
                </a>
                <a
                  href="https://github.com/FabriceGhislain7"
                  target="_blank"
                  rel="noreferrer"
                  className="btn btn-outline-warning btn-sm me-2 mb-2"
                  onClick={handleSparkle}
                >
                  <i className="bi bi-github me-1"></i>GitHub
                </a>
                <a
                  href="tel:+393519957025"
                  className="btn btn-outline-warning btn-sm mb-2"
                  onClick={handleSparkle}
                >
                  <i className="bi bi-telephone me-1"></i>Telefono
                </a>
              </div>
            </div>
          </div>
        </div>
      </div>
    </footer>
  )
}

export default Footer
