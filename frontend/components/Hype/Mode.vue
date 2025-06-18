<style>
.border:focus {
  outline: none;
  box-shadow: 0 0 1px var(--accent);
}
</style>
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
      'relative -left-2',
      'text-lg flex gap-4 rounded-lg p-2 border border-transparent',
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
