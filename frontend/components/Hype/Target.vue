<script setup lang="ts">
defineProps<{ target: string }>();
const isDark = useDarkCheck();
const emit = defineEmits<{
  (e: 'update:target', value: string): void;
}>();
</script>

<template>
  <label
    :class="
      cn(
        'flex items-center',
        'w-full p-4 rounded-xl resize-none',
        'focus:ring-0 focus:outline-none focus:border-0',
        isDark
          ? 'bg-[#1e1e1e] focus:bg-[#222] text-white placeholder-neutral-100 shadow-inner-neumorphic-dark'
          : 'bg-[#e0e0e0] focus:bg-[#d1d1d1] text-gray-800 placeholder-black shadow-inner-neumorphic',
      )
    "
  >
    <input
      :class="cn('text-lg w-full', 'focus:ring-0 focus:outline-none focus:border-0')"
      v-if="isDark !== null"
      :value="target"
      @input="(e) => emit('update:target', (e.target as HTMLTextAreaElement).value)"
      placeholder="Target"
    />
    <button
      v-if="Boolean(target)"
      class="cursor-pointer text-current"
      @click="
        () => {
          emit('update:target', '');
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
</style>
