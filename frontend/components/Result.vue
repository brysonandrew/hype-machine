<script setup lang="ts">
const { typedOutput } = useTypewriter();
</script>

<template>
  <div
    v-if="typedOutput"
    class="w-full p-4 text-lg rounded-2xl bg-white dark:bg-neutral-900 text-neutral-800 dark:text-neutral-100 shadow-md whitespace-pre-wrap transition"
  >
    {{ typedOutput }}
  </div>
</template>
