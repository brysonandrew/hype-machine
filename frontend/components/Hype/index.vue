<script setup lang="ts">
const { prompt, isLoading, click } = useHype();
</script>
<template>
  <HypePrompt
    v-model:prompt="prompt"
    @submit="click"
  />
  <HypeButton
    :is-loading="isLoading"
    :is-empty="!prompt"
    @click="click"
  >
    {{ isLoading ? 'Generating...' : "Let's go" }}
    <template #icon>
      <IconsSiren />
    </template>
  </HypeButton>
</template>
