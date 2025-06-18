export const useTypewriter = () => {
  const typedTokens = useState<string[]>('typed-tokens', () => []);
  const typingIndex = useState('typing-index', () => 0);

  const tokenizeText = (text: string): string[] => {
    return text.match(/(\S+\s*|\n+)/g) || [];
  };

  const animateTyping = (text: string, ms = 200) => {
    const tokens = tokenizeText(text);
    typedTokens.value = [];
    typingIndex.value = 0;

    const interval = setInterval(() => {
      if (typingIndex.value < tokens.length) {
        typedTokens.value.push(tokens[typingIndex.value]);
        typingIndex.value++;
      } else {
        clearInterval(interval);
      }
    }, ms);
  };

  return { typedTokens, animateTyping };
};