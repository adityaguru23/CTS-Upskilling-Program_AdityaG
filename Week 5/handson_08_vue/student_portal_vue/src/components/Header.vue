<script setup>
import { RouterLink } from 'vue-router';
import { useEnrollmentStore } from '../stores/enrollment';

const store = useEnrollmentStore();
</script>

<template>
  <header style="display: flex; justify-content: space-between; padding: 1rem;">
    <h1>Student Portal</h1>
    <nav style="display: flex; gap: 1rem;">
      <RouterLink to="/">Home</RouterLink>
      <RouterLink to="/courses">Courses</RouterLink>
      <RouterLink to="/profile">Profile ({{ store.enrolledCourses.length }})</RouterLink>
    </nav>
  </header>
</template>