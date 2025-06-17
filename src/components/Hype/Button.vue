<script setup lang="ts">
defineProps<{ isLoading: boolean; isEmpty: boolean }>();
const isDark = useDarkCheck();
</script>

<template>
  <button
    v-if="isDark !== null"
    @click="$emit('click')"
    :disabled="isLoading || isEmpty"
    :class="
      cn(
        'flex gap-2 uppercase text-lg',
        'relative overflow-hidden group px-8 py-3 rounded-2xl font-semibold transition duration-200 ease-in-out cursor-pointer disabled:cursor-not-allowed',
        isEmpty ? 'opacity-20' : 'btn-gradient-hover ',
        isLoading ? 'btn-gradient-hover btn-gradient-hover-on' : 'btn-gradient-hover-off',
        isDark
          ? 'bg-[#1e1e1e] text-white shadow-neumorphic-dark hover:shadow-neumorphic-hover-dark active:shadow-neumorphic-inset-dark'
          : 'bg-[#e0e0e0] text-gray-800 shadow-neumorphic hover:shadow-neumorphic-hover active:shadow-neumorphic-inset',
      )
    "
  >
    <slot />
    <div :class="cn(isEmpty ? '' : 'group-hover:-rotate-45', isLoading && '-rotate-45')">
      <slot name="icon" />
    </div>
  </button>
</template>

<style scoped>
/* Light mode: soft neumorphism */
.shadow-neumorphic {
  box-shadow: 4px 4px 8px #bebebe, -4px -4px 8px #ffffff;
}

.shadow-neumorphic-hover {
  box-shadow: 6px 6px 12px #bebebe, -6px -6px 12px #ffffff;
}

.shadow-neumorphic-inset {
  box-shadow: inset 2px 2px 6px #bebebe, inset -2px -2px 6px #ffffff;
}

/* Dark mode: subtle neumorphism */
.shadow-neumorphic-dark {
  box-shadow: 3px 3px 6px #0f0f0f, -3px -3px 6px #2b2b2b;
}

.shadow-neumorphic-hover-dark {
  box-shadow: 5px 5px 10px #0f0f0f, -5px -5px 10px #2b2b2b;
}

.shadow-neumorphic-inset-dark {
  box-shadow: inset 2px 2px 4px #0f0f0f, inset -2px -2px 4px #2b2b2b;
}
.btn-gradient-hover::before {
  content: '';
  position: absolute;
  inset: 0;
  z-index: 0;
  background: linear-gradient(
    120deg,
    rgba(255, 0, 150, 0.25),
    rgba(0, 255, 255, 0.25),
    rgba(255, 255, 0, 0.25),
    rgba(255, 0, 255, 0.25)
  );
  background-size: 300% 300%;
  transform: scale(1.5);
  transition: opacity 0.4s ease;
  animation: bg-shimmer 4s ease-in-out infinite;
  pointer-events: none;
  border-radius: inherit;
}

.btn-gradient-hover-off::before {
  opacity: 0;
}

.btn-gradient-hover:hover::before {
  opacity: 1;
}

.btn-gradient-hover > * {
  position: relative;
  z-index: 1;
}

@keyframes bg-shimmer {
  0% {
    background-position: 0% 50%;
  }
  50% {
    background-position: 100% 50%;
  }
  100% {
    background-position: 0% 50%;
  }
}

.pulse-echo {
  width: 24px;
  height: 24px;
  opacity: 0.5;
  border-radius: 9999px;
  background: #39ff14; /* bright green or any accent */
  position: relative;
  animation: pulse-core 2s infinite ease-in-out;
}

.pulse-echo::before,
.pulse-echo::after {
  content: '';
  position: absolute;
  inset: 0;
  border-radius: 9999px;
  background: inherit;
  opacity: 0.6;
  animation: echo-ring 2s infinite ease-out;
}

.pulse-echo::after {
  animation-delay: 1s;
}

@keyframes pulse-core {
  0%,
  100% {
    transform: scale(1);
    box-shadow: 0 0 8px #39ff14, 0 0 16px #00fff7;
  }
  50% {
    transform: scale(1.1);
    box-shadow: 0 0 16px #39ff14, 0 0 32px #00fff7;
  }
}

@keyframes echo-ring {
  0% {
    transform: scale(1);
    opacity: 0.4;
  }
  100% {
    transform: scale(2.5);
    opacity: 0;
  }
}
</style>
