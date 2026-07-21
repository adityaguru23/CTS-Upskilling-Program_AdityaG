import { configureStore } from '@reduxjs/toolkit';
import enrollmentReducer from './stores/enrollmentSlice';

export const store = configureStore({
  reducer: {
    enrollment: enrollmentReducer,
  },
});