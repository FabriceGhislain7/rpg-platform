import Navbar from '../Navbar/Navbar'
import Footer from '../Footer/Footer'
import './MainLayout.css'

function MainLayout({ children, isAuthenticated = false, user = null, currentPath = '/' }) {
  return (
    <div className="app-shell d-flex flex-column min-vh-100">
      <Navbar isAuthenticated={isAuthenticated} user={user} currentPath={currentPath} />
      <main className="app-main flex-grow-1">
        {children}
      </main>
      <Footer isAuthenticated={isAuthenticated} />
    </div>
  )
}

export default MainLayout
