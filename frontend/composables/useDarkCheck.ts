export const useDarkCheck = () => {
  const colorMode = useColorMode();

  const isDark = ref(false);

  watchEffect(() => {
    const next = colorMode.value === 'dark';
    isDark.value = next;
  });

  return isDark;
};
