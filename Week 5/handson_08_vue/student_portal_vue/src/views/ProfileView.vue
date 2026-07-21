<script setup>
import { useEnrollmentStore } from '../stores/enrollment';

const store = useEnrollmentStore();
</script>

<template>
  <div>
    <h2>Student Profile</h2>
    <p>Total Credits: {{ store.totalCredits }}</p>

    <h3>Enrolled Courses</h3>
    <ul>
      <li v-for="course in store.enrolledCourses" :key="course.id">
        {{ course.name }} - {{ course.credits }} Credits
        <button @click="store.unenroll(course.id)">Remove</button>
      </li>
    </ul>
  </div>
</template>