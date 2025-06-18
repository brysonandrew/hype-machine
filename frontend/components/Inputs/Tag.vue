<script setup lang="ts">
import { ref, watch, computed } from 'vue';

interface Props {
  modelValue: string[];
}

const props = defineProps<Props>();
const emit = defineEmits<{
  (e: 'update:modelValue', value: string[]): void;
}>();

const input = ref<string>('');
const tags = ref<string[]>([...props.modelValue]);
const inputRef = ref<HTMLInputElement | null>(null);

watch(
  () => props.modelValue,
  (newVal) => {
    tags.value = [...newVal];
  },
);

function addTag(): void {
  const newTag = input.value.trim();
  if (newTag && !tags.value.includes(newTag)) {
    tags.value.push(newTag);
    emit('update:modelValue', tags.value);
    const element = inputRef.value;
    if (element) {
      element.focus();
    }
  }
  input.value = '';
}

function removeTag(index: number): void {
  tags.value.splice(index, 1);
  emit('update:modelValue', tags.value);
}

function removeLastTag(): void {
  if (!input.value && tags.value.length > 0) {
    tags.value.pop();
    emit('update:modelValue', tags.value);
  }
}

const isDark = useDarkCheck();
</script>

<template>
  <div :class="['tag-input text-lg text-black dark:text-white', isDark ? 'dark' : 'light']">
    <div
      v-if="tags.length > 0"
      class="tags"
    >
      <span
        v-for="(tag, index) in tags"
        :key="index"
        class="tag"
      >
        {{ tag }}
        <button @click="removeTag(index)">
          <svg
            xmlns="http://www.w3.org/2000/svg"
            width="24px"
            height="24px"
            viewBox="0 0 16 16"
          >
            <path
              fill="none"
              stroke="currentColor"
              stroke-linecap="round"
              stroke-linejoin="round"
              stroke-width="1.5"
              d="m11.25 4.75l-6.5 6.5m0-6.5l6.5 6.5"
            />
          </svg>
        </button>
      </span>
    </div>
    <label class="flex gap-4">
      <input
        v-model="input"
        @keyup.enter="addTag"
        @blur="addTag"
        @keydown.delete="removeLastTag"
        placeholder="Tone"
        class="placeholder-black dark:placeholder-white text-lg"
        ref="inputRef"
      />
      <button
        v-if="Boolean(input)"
        class="cursor-pointer cross"
        @click="
          () => {
            input = '';
          }
        "
      >
        <IconsCross />
      </button>
      <button
        @click="addTag"
        class="cursor-pointer plus"
      >
        <IconsPlus />
      </button>
    </label>
  </div>
</template>

<style scoped>
/* Light Mode */
.tag-input.light {
  --bg: #e0e0e0;
  --shadow-light: #ffffff;
  --shadow-dark: #bebebe;
}

/* Dark Mode */
.tag-input.dark {
  --bg: #1e1e1e;
  --shadow-light: #2a2a2a;
  --shadow-dark: #141414;
}

.tag-input {
  display: flex;
  flex-wrap: wrap;
  align-items: center;
  gap: 0.5rem;
  background: var(--bg);
  border-radius: 12px;
  padding: 0.25rem;
  box-shadow: 6px 6px 12px var(--shadow-dark), -6px -6px 12px var(--shadow-light);
}

.tags {
  display: flex;
  flex-wrap: wrap;
  gap: 0.5rem;
}

.tag {
  background: var(--bg);
  padding: 0.75rem 1.25rem;
  border-radius: 2rem;
  box-shadow: inset 2px 2px 5px var(--shadow-dark), inset -2px -2px 5px var(--shadow-light);
  display: flex;
  align-items: center;
  gap: 8px;
  color: var(--text);
}

.tag button {
  background: none;
  border: none;
  font-weight: bold;
  cursor: pointer;
  color: var(--text);
}

input {
  flex-grow: 1;
  border: none;
  outline: none;
}

label {
  flex-grow: 1;
  padding: 0.75rem 1.25rem;
  border-radius: 10px;
  background-color: var(--bg);
  box-shadow: inset 2px 2px 5px var(--shadow-dark), inset -2px -2px 5px var(--shadow-light);
  color: var(--text);
}

label button.plus svg {
  color: var(--accent);
}
</style>
