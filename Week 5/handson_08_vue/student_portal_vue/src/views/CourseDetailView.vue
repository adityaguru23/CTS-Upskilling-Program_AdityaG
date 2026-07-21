<script setup>
import { useRoute, useRouter } from 'vue-router';

const route = useRoute();
const router = useRouter();

const handleEnrollRedirect = () => {
  router.push('/profile');
};
</script>

<template>
  <div>
    <h2>Course Details for ID: {{ route.params.id }}</h2>
    <button @click="handleEnrollRedirect">Enroll</button>
  </div>
</template>