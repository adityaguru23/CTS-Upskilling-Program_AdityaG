<script setup>
defineProps({
  name: String,
  code: String,
  credits: Number,
  grade: String
});

defineEmits(['enroll']);
</script>

<template>
  <article class="course-card">
    <h3>{{ name }}</h3>
    <p>Code: {{ code }}</p>
    <span>Credits: {{ credits }}</span>
    <button @click="$emit('enroll')">Enroll</button>
  </article>
</template>