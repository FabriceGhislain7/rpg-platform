import Navbar from './components/Navbar/Navbar'
import Footer from './components/Footer/Footer'

function App() {
  return (
    <div className="d-flex flex-column min-vh-100">
      <Navbar isAuthenticated={false} currentPath="/" />
      <main className="flex-grow-1" style={{ paddingTop: '90px' }}>
        {/* contenuto pagina */}
      </main>
      <Footer isAuthenticated={false} />
    </div>
  )
}

export default App
