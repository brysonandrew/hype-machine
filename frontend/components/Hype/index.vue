<script setup lang="ts">
const { target, context, isLoading, click } = useHype();
</script>
<template>
  <div class="flex flex-col items-stretch justify-center gap-8 py-4 grow">
    <div class="flex flex-col items-center gap-8 md:flex-row">
      <HypeMode />
      <HypeTarget v-model:target="target" />
    </div>
    <HypeContext
      v-model:context="context"
      @submit="click"
    />
    <HypeButton
      :is-loading="isLoading"
      :is-empty="!context"
      @click="click"
    >
      {{ isLoading ? 'Generating...' : "Let's go" }}
      <template #icon>
        <IconsSiren />
      </template>
    </HypeButton>
  </div>
</template>
