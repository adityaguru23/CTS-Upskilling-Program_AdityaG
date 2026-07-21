import { Routes, Route } from 'react-router-dom';
import Header from './components/Header';
import CoursesPage from './pages/CoursesPage';
import ProfilePage from './pages/ProfilePage';

function App() {
  return (
    <>
      <Header siteName="Student Portal" />
      <main>
        <Routes>
          <Route path="/courses" element={<CoursesPage />} />
          <Route path="/profile" element={<ProfilePage />} />
        </Routes>
      </main>
    </>
  );
}

export default App;