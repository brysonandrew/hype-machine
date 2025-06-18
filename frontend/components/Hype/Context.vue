<script setup lang="ts">
defineProps<{ context: string }>();
const isDark = useDarkCheck();
const emit = defineEmits<{
  (e: 'update:context', value: string): void;
  (e: 'submit'): void;
}>();

const handleKeyDown = (e: KeyboardEvent) => {
  if (e.key === 'Enter' && !e.shiftKey) {
    e.preventDefault();
    emit('submit');
  }
};
</script>

<template>
  <label
    :class="
      cn(
        'flex focus:outline-0 focus:border-0 items-start',
        'text-lg w-full p-4 rounded-xl resize-none transition duration-200 ease-in-out',
        'focus:ring-0 focus:outline-none focus:border-0',
        isDark
          ? 'bg-[#1e1e1e] focus:bg-[#222] text-white placeholder-neutral-100 shadow-inner-neumorphic-dark'
          : 'bg-[#e0e0e0] focus:bg-[#d1d1d1] text-gray-800 placeholder-black shadow-inner-neumorphic',
      )
    "
  >
    <textarea
      :class="cn('w-full')"
      v-if="isDark !== null"
      :value="context"
      @input="(e) => $emit('update:context', (e.target as HTMLTextAreaElement).value)"
      @keydown="handleKeyDown"
      rows="4"
      placeholder="Context"
    />
    <button
      v-if="Boolean(context)"
      class="cursor-pointer text-current"
      @click="
        () => {
          emit('update:context', '');
        }
      "
    >
      <IconsCross />
    </button>
  </label>
</template>
<style scoped>
.shadow-inner-neumorphic {
  box-shadow: inset 4px 4px 8px #bebebe, inset -4px -4px 8px #ffffff;
}
.shadow-inner-neumorphic-dark {
  box-shadow: inset 1px 1px 3px rgba(255, 255, 255, 0.05), inset -1px -1px 3px rgba(0, 0, 0, 0.3);
}
textarea {
  outline: none;
  border: none;
}

textarea:focus {
  box-shadow: 0 0 0 0 transparent; /* Tailwind blue-500, for example */
}
</style>
