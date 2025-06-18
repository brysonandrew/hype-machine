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
  <div
    tabindex="0"
    @keydown="handleKeyDown"
    :class="[
      'text-lg flex gap-4 rounded-lg p-2 focus:outline-0 focus:bg-gray-200 dark:focus:bg-gray-800',
      isDark ? 'text-white' : 'text-black',
    ]"
  >
    <InputsRadio
      value="promote"
      :active="mode"
    >
      Promote
    </InputsRadio>
    <InputsRadio
      value="trash-talk"
      :active="mode"
      v-model="mode"
    >
      Trash Talk
    </InputsRadio>
  </div>
</template>
