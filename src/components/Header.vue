<script setup lang="ts">
import { ref, onMounted } from 'vue';

const isGlitching = ref(true);
const isDark = useDarkCheck();

let timeoutId: ReturnType<typeof setTimeout>;

onMounted(() => {
  timeoutId = setTimeout(() => {
    isGlitching.value = false;
  }, 8000);
});

onBeforeUnmount(() => {
  clearTimeout(timeoutId);
});

const textClassValue = 'text-9xl font-bold tracking-normal';
</script>

<template>
  <header
    v-if="isDark !== null"
    class="-left-24 px-24 w-full flex flex-col justify-between items-center lg:flex-row relative overflow-hidden"
  >
    <Container>
      <span
        v-for="n in 10"
        :key="n"
        class="absolute top-0 left-0 w-full pointer-events-none select-none"
        :class="isGlitching ? `glitch-layer glitch-${n} slide-in-${n}` : 'hidden'"
      >
        <span :class="cn(textClassValue)"> Hype Machine </span>
      </span>

      <h1
        :class="
          cn('relative z-10', textClassValue, isDark ? 'text-neumorphic-dark' : 'text-neumorphic')
        "
      >
        Hype Machine
      </h1>
    </Container>
  </header>
</template>

<style scoped>
.text-neumorphic {
  color: #333;

  text-shadow: 4px 4px 8px #b0b0b0, /* stronger lower-right shadow */ -4px -4px 8px #ffffff; /* brighter upper-left highlight */
}

.text-neumorphic-dark {
  color: #eee;
  text-shadow: 4px 4px 8px #000000, -4px -4px 8px #3c3c3c;
}

@keyframes glitch-float {
  0% {
    transform: translate(0, 0);
    opacity: 1;
  }
  50% {
    transform: translate(var(--x), var(--y));
    opacity: 0.8;
  }
  100% {
    transform: translate(0, 0);
    opacity: 1;
  }
}

@keyframes slide-in-left {
  0% {
    transform: translateX(-6rem);
    opacity: 0;
  }
  60% {
    opacity: 1;
  }
  100% {
    transform: translateX(0);
  }
}

.glitch-layer {
  z-index: 5;
  mix-blend-mode: difference;
  animation: glitch-float 0.6s infinite ease-in-out;
}

/* Unique, staggered color per layer */
.glitch-1 {
  --x: 1px;
  --y: -1px;
  animation-delay: 0s;
  color: #ff3b3b;
} /* red */
.glitch-2 {
  --x: -2px;
  --y: 2px;
  animation-delay: 0.05s;
  color: #00fff7;
} /* cyan */
.glitch-3 {
  --x: 3px;
  --y: -1px;
  animation-delay: 0.1s;
  color: #7fff00;
} /* lime */
.glitch-4 {
  --x: -3px;
  --y: 1px;
  animation-delay: 0.15s;
  color: #ffee00;
} /* yellow */
.glitch-5 {
  --x: 1px;
  --y: 3px;
  animation-delay: 0.2s;
  color: #ff8bff;
} /* pink */
.glitch-6 {
  --x: -1px;
  --y: -3px;
  animation-delay: 0.25s;
  color: #6ecbff;
} /* light blue */
.glitch-7 {
  --x: 2px;
  --y: 1px;
  animation-delay: 0.3s;
  color: #ff6600;
} /* orange */
.glitch-8 {
  --x: -2px;
  --y: 2px;
  animation-delay: 0.35s;
  color: #9400ff;
} /* violet */
.glitch-9 {
  --x: 0px;
  --y: -2px;
  animation-delay: 0.4s;
  color: #32ffdd;
} /* turquoise */
.glitch-10 {
  --x: 1px;
  --y: 2px;
  animation-delay: 0.45s;
  color: #ff1a75;
} /* hot pink */

.slide-in-1 {
  animation: slide-in-left 0.8s ease-out 0s forwards;
}
.slide-in-2 {
  animation: slide-in-left 0.8s ease-out 0.05s forwards;
}
.slide-in-3 {
  animation: slide-in-left 0.8s ease-out 0.1s forwards;
}
.slide-in-4 {
  animation: slide-in-left 0.8s ease-out 0.15s forwards;
}
.slide-in-5 {
  animation: slide-in-left 0.8s ease-out 0.2s forwards;
}
.slide-in-6 {
  animation: slide-in-left 0.8s ease-out 0.25s forwards;
}
.slide-in-7 {
  animation: slide-in-left 0.8s ease-out 0.3s forwards;
}
.slide-in-8 {
  animation: slide-in-left 0.8s ease-out 0.35s forwards;
}
.slide-in-9 {
  animation: slide-in-left 0.8s ease-out 0.4s forwards;
}
.slide-in-10 {
  animation: slide-in-left 0.8s ease-out 0.45s forwards;
}
</style>
