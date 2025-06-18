export const useTypewriter = () => {
  const typedOutput = useState('typed-output', () => '');
  const typingIndex = useState('typing-index', () => 0);

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
