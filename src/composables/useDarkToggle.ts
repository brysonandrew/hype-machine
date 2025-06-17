import { useColorMode } from '#imports';

export const useDarkToggle = () => {
  const colorMode = useColorMode()

  const isDark = useDarkCheck()

  const toggleDark = () => {
    colorMode.preference = isDark.value ? 'light' : 'dark'
  }

  return toggleDark;
};
