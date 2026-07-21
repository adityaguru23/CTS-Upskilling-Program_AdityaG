<script setup>
import { ref, onMounted, computed } from 'vue';
import { useEnrollmentStore } from '../stores/enrollment';
import CourseCard from '../components/CourseCard.vue';
import { useRouter } from 'vue-router';
import axios from 'axios';

const courses = ref([]);
const searchTerm = ref('');
const store = useEnrollmentStore();
const router = useRouter();

onMounted(async () => {
  const response = await axios.get('https://jsonplaceholder.typicode.com/posts?_limit=5');
  courses.value = response.data.map(item => ({
    id: item.id,
    name: item.title,
    credits: 4
  }));
});

const filteredCourses = computed(() => {
  return courses.value.filter(c => c.name.toLowerCase().includes(searchTerm.value.toLowerCase()));
});

const handleEnroll = (course) => {
  store.enroll(course);
  router.push('/profile');
};
</script>

<template>
  <div>
    <input v-model="searchTerm" placeholder="Search courses..." />
    <div class="course-grid">
      <CourseCard
        v-for="course in filteredCourses"
        :key="course.id"
        :name="course.name"
        :credits="course.credits"
        @enroll="handleEnroll(course)"
      />
    </div>
  </div>
</template>