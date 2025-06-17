import { ref } from 'vue';

export const useTypewriter = () => {
  const typedOutput = ref('');
  const typingIndex = ref(0);

  const animateTyping = (text: string, ms = 100) => {
    typedOutput.value = '';
    typingIndex.value = 0;
    const words = text.split(/\s/g);
    const interval = setInterval(() => {
      if (typingIndex.value < words.length) {
        typedOutput.value = `${typedOutput.value} ${words[typingIndex.value]}`;
        typingIndex.value++;
      } else {
        clearInterval(interval);
      }
    }, ms);
  };

  return { typedOutput, animateTyping };
};
