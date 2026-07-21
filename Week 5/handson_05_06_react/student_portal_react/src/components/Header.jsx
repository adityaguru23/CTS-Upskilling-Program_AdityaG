import { Link } from 'react-router-dom';
import { useSelector } from 'react-redux';

function Header({ siteName }) {
  const enrolledCourses = useSelector(state => state.enrollment.enrolledCourses);

  return (
    <header style={{ display: 'flex', justifyContent: 'space-between', padding: '1rem' }}>
      <h1>{siteName}</h1>
      <nav style={{ display: 'flex', gap: '1rem' }}>
        <Link to="/courses">Courses</Link>
        <Link to="/profile">Profile ({enrolledCourses.length})</Link>
      </nav>
    </header>
  );
}

export default Header;