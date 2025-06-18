<script setup lang="ts">
const mode = useMode();
const isDark = useDarkCheck();
</script>

<template>
  <div :class="['text-lg', isDark ? 'text-gray-100' : 'text-black']">
    <div class="flex gap-4">
      <InputsRadio
        value="promote"
        :active="mode"
      >
        Promote</InputsRadio
      >
      <InputsRadio
        value="trash-talk"
        :active="mode"
      >
        Trash Talk</InputsRadio
      >
    </div>
  </div>
</template>
