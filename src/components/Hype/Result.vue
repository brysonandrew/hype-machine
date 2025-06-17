<script setup lang="ts">
defineProps<{ text: string }>();
</script>

<template>
  <div
    v-if="text"
    class="w-full p-4 text-lg rounded-2xl bg-white dark:bg-neutral-900 text-neutral-800 dark:text-neutral-100 shadow-md whitespace-pre-wrap transition"
  >
    {{ text }}
  </div>
</template>
