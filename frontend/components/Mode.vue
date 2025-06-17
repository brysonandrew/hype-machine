<script setup>
const mode = useMode();
const isDark = useDarkCheck();
</script>

<template>
  <div :class="['flex flex-col gap-6 p-6 text-lg', isDark ? 'text-gray-100' : 'text-black']">
    <div class="flex gap-4">
      <label
        :class="['neumorphic-label', isDark ? 'dark' : 'light', { selected: mode === 'happy' }]"
      >
        <input
          type="radio"
          value="happy"
          v-model="mode"
        />
        <svg
          xmlns="http://www.w3.org/2000/svg"
          width="24px"
          height="24px"
          viewBox="0 0 24 24"
        >
          <path
            fill="currentColor"
            d="M7.24 11v9H5.63c-.9 0-1.62-.72-1.62-1.61v-5.77c0-.89.73-1.62 1.62-1.62zM18.5 9.5h-4.78V6c0-1.1-.9-2-1.99-2h-.09c-.4 0-.76.24-.92.61L7.99 11v9h9.2c.73 0 1.35-.52 1.48-1.24l1.32-7.5c.16-.92-.54-1.76-1.48-1.76Z"
          />
        </svg>
        Promoter
      </label>

      <label :class="['neumorphic-label', isDark ? 'dark' : 'light', { selected: mode === 'sad' }]">
        <input
          type="radio"
          value="sad"
          v-model="mode"
        />
        <svg
          xmlns="http://www.w3.org/2000/svg"
          width="24px"
          height="24px"
          viewBox="0 0 24 24"
        >
          <path
            fill="currentColor"
            d="M20 5.61v5.77c0 .89-.73 1.62-1.62 1.62h-1.61V4h1.61c.9 0 1.62.72 1.62 1.61M5.34 5.24l-1.32 7.5c-.16.92.54 1.76 1.48 1.76h4.78V18c0 1.1.9 2 1.99 2h.09c.4 0 .76-.24.92-.61L16.01 13V4h-9.2c-.73 0-1.35.52-1.48 1.24Z"
          />
        </svg>
        Trash Talker
      </label>
    </div>
  </div>
</template>

<style scoped>
.neumorphic-label {
  display: flex;
  align-items: center;
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
