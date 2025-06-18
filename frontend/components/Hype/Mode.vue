<script setup lang="ts">
const mode = useMode();
const isDark = useDarkCheck();
const handleKeyDown = (event: KeyboardEvent) => {
  if (event.key === 'Enter') {
    mode.value = mode.value === 'promote' ? 'trash-talk' : 'promote';
  }
};
</script>

<template>
  <div :class="['text-lg', isDark ? 'text-white' : 'text-black']">
    <div
      tabindex="0"
      @keydown="handleKeyDown"
      class="flex gap-4 rounded-lg focus:outline-1"
    >
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
