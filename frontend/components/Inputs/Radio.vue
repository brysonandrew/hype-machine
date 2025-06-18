<script setup lang="ts">
type TProps<T extends string> = { value: T; active: T };
defineProps<TProps<string>>();
const mode = useMode();
const isDark = useDarkCheck();
</script>

<template>
  <label :class="['neumorphic-label', isDark ? 'dark' : 'light', { selected: value === active }]">
    <input
      type="radio"
      :value="value"
      v-model="mode"
    />
    <slot />
  </label>
</template>

<style scoped>
.neumorphic-label {
  display: flex;
  align-items: center;
  white-space: nowrap;
  gap: 0.5rem;
  padding: 1rem 1.5rem;
  border-radius: 12px;
  cursor: pointer;
  transition: all 0.2s ease-in-out;
  opacity: 0.5;
}

.neumorphic-label.selected {
  opacity: 1;
}
/* Hide native radio */
.neumorphic-label input[type='radio'] {
  display: none;
}

/* Light mode styles */
.neumorphic-label.light {
  background: #e0e0e0;
  color: #333;
  box-shadow: 6px 6px 12px #bebebe, -6px -6px 12px #ffffff;
}

.neumorphic-label.light.selected {
  box-shadow: inset 6px 6px 12px #bebebe, inset -6px -6px 12px #ffffff;
}

/* Dark mode styles: deeper & subtle */
.neumorphic-label.dark {
  background: #1c1c1c;
  color: #ccc;
  box-shadow: 4px 4px 8px #141414, -4px -4px 8px #222222;
}

.neumorphic-label.dark.selected {
  box-shadow: inset 4px 4px 8px #141414, inset -4px -4px 8px #222222;
}
</style>
