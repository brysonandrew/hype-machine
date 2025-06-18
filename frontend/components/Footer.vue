<script setup lang="ts">
const toggleDarkMode = useDarkToggle();
const isDark = useDarkCheck();
const printPage = () => {
  window.print();
};
</script>

<template>
  <footer class="fixed bottom-4 w-full flex items-end justify-end gap-2 h-0 px-4 no-print">
    <button
      tabindex="-1"
      @click="printPage"
      :class="[
        'aspect-square w-12 p-3 rounded-full transition duration-200 ease-in-out cursor-pointer',
        isDark
          ? 'bg-[#252525] text-white shadow-neumorphic-dark hover:shadow-neumorphic-hover-dark active:shadow-neumorphic-inset-dark'
          : 'bg-[#e0e0e0] text-black shadow-neumorphic hover:shadow-neumorphic-hover active:shadow-neumorphic-inset',
      ]"
    >
      <svg
        xmlns="http://www.w3.org/2000/svg"
        width="24px"
        height="24px"
        viewBox="0 0 24 24"
      >
        <path
          fill="currentColor"
          d="M21 7v12q0 .825-.587 1.413T19 21H5q-.825 0-1.412-.587T3 19V5q0-.825.588-1.412T5 3h12zm-9 11q1.25 0 2.125-.875T15 15t-.875-2.125T12 12t-2.125.875T9 15t.875 2.125T12 18m-6-8h9V6H6z"
        />
      </svg>
    </button>
    <button
      tabindex="-1"
      @click="toggleDarkMode"
      :class="[
        'aspect-square w-12 p-3 rounded-full transition duration-200 ease-in-out cursor-pointer',
        isDark
          ? 'bg-[#252525] text-white shadow-neumorphic-dark hover:shadow-neumorphic-hover-dark active:shadow-neumorphic-inset-dark'
          : 'bg-[#e0e0e0] text-black shadow-neumorphic hover:shadow-neumorphic-hover active:shadow-neumorphic-inset',
      ]"
    >
      <!-- Moon SVG -->
      <svg
        v-if="isDark"
        xmlns="http://www.w3.org/2000/svg"
        fill="currentColor"
        viewBox="0 0 24 24"
      >
        <path d="M21 12.79A9 9 0 1111.21 3 7 7 0 0021 12.79z" />
      </svg>
      <!-- Sun SVG -->
      <svg
        v-else
        xmlns="http://www.w3.org/2000/svg"
        fill="currentColor"
        viewBox="0 0 24 24"
      >
        <path
          d="M12 18a6 6 0 100-12 6 6 0 000 12zm0 4a1 1 0 011 1h-2a1 1 0 011-1zm0-20a1 1 0 011-1h-2a1 1 0 011 1zm10 10a1 1 0 011 1v-2a1 1 0 01-1 1zm-20 0a1 1 0 011 1v-2a1 1 0 01-1 1zm16.95 7.05a1 1 0 011.41 0l-1.42 1.42a1 1 0 010-1.42zM4.05 4.05a1 1 0 011.41 0L4.05 5.47a1 1 0 010-1.42zm15.9-1.41a1 1 0 010 1.42l-1.42-1.42a1 1 0 011.42 0zM4.05 19.95a1 1 0 010-1.42l1.42 1.42a1 1 0 01-1.42 0z"
        />
      </svg>
    </button>
  </footer>
</template>

<style>
/* Light mode */
.shadow-neumorphic {
  box-shadow: 4px 4px 8px #bebebe, -4px -4px 8px #ffffff;
}
.shadow-neumorphic-hover {
  box-shadow: 6px 6px 12px #bebebe, -6px -6px 12px #ffffff;
}
.shadow-neumorphic-inset {
  box-shadow: inset 2px 2px 6px #bebebe, inset -2px -2px 6px #ffffff;
}

/* Dark mode */
.shadow-neumorphic-dark {
  box-shadow: 2px 2px 6px #0f0f0f, -2px -2px 6px #2b2b2b;
}
.shadow-neumorphic-hover-dark {
  box-shadow: 3px 3px 8px #0f0f0f, -3px -3px 8px #2b2b2b;
}
.shadow-neumorphic-inset-dark {
  box-shadow: inset 2px 2px 4px #0f0f0f, inset -2px -2px 4px #2b2b2b;
}
</style>
