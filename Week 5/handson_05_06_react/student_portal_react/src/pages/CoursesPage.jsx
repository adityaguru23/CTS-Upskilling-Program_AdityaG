import { useState, useEffect } from 'react';
import axios from 'axios';
import CourseCard from '../components/CourseCard';

function CoursesPage() {
  const [courses, setCourses] = useState([]);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState(null);
  const [searchTerm, setSearchTerm] = useState('');

  useEffect(() => {
    axios.get('https://jsonplaceholder.typicode.com/posts?_limit=5')
      .then(response => {
        const formatted = response.data.map(item => ({
          id: item.id,
          name: item.title,
          code: `CS${item.id}00`,
          credits: 4,
          grade: 'N/A'
        }));
        setCourses(formatted);
        setLoading(false);
      })
      .catch(err => {
        setError(err.message);
        setLoading(false);
      });
  }, []);

  const filtered = courses.filter(c => c.name.toLowerCase().includes(searchTerm.toLowerCase()));

  if (loading) return <p>Loading courses...</p>;
  if (error) return <p>Error: {error}</p>;

  return (
    <div>
      <input
        type="text"
        placeholder="Search courses..."
        value={searchTerm}
        onChange={(e) => setSearchTerm(e.target.value)}
      />
      <div className="course-grid">
        {filtered.map(course => (
          <CourseCard key={course.id} {...course} />
        ))}
      </div>
    </div>
  );
}

export default CoursesPage;