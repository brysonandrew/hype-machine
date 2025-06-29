import tailwindcss from '@tailwindcss/vite';

export default defineNuxtConfig({
  modules: ['@nuxtjs/color-mode'],
  colorMode: {
    preference: 'system', // default theme
    fallback: 'dark', // fallback if system preference can't be detected
    classSuffix: '', // removes `-mode` suffix from class
  },
  devtools: { enabled: true },
  srcDir: '.',
  imports: {
    dirs: ['./constants', './components', './composables', './types', './utils'],
  },
  css: ['~/public/css/main.css'],
  vite: {
    plugins: [tailwindcss()],
  },
  nitro: {
    compatibilityDate: '2025-06-16',
  },
});
