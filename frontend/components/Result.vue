<script setup lang="ts">
import { motion } from 'motion-v';
const { typedTokens } = useTypewriter();
</script>

<template>
  <div
    v-if="typedTokens.length > 0"
    class="w-full p-4 text-lg rounded-2xl bg-white dark:bg-neutral-900 text-neutral-800 dark:text-neutral-100 shadow-md whitespace-pre-wrap transition"
  >
    <div class="typewriter-output">
      <motion.div
        v-for="(token, index) in typedTokens"
        :key="index"
        :initial="{ opacity: 0, y: 1 }"
        :animate="{ opacity: 1, y: 0 }"
        :transition="{ delay: index * 0.04 }"
        class="token"
      >
        {{ token }}
      </motion.div>
    </div>
  </div>
</template>
<style scoped>
.typewriter-output {
  display: flex;
  flex-wrap: wrap;
  align-items: flex-start;
}

.token {
  white-space: pre-wrap;
}
</style>
