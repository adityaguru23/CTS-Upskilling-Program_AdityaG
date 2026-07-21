import { useDispatch } from 'react-redux';
import { useNavigate } from 'react-router-dom';
import { enroll } from '../stores/enrollmentSlice';

function CourseCard({ id, name, code, credits, grade }) {
  const dispatch = useDispatch();
  const navigate = useNavigate();

  const handleEnroll = () => {
    dispatch(enroll({ id, name, code, credits, grade }));
    navigate('/profile');
  };

  return (
    <article className="course-card">
      <h3>{name}</h3>
      <p>Code: {code}</p>
      <span>Credits: {credits}</span>
      <button onClick={handleEnroll}>Enroll</button>
    </article>
  );
}

export default CourseCard;