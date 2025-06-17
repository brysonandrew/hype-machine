import { ref } from 'vue';
import { useTypewriter } from './useTypewriter';

export const useHype = () => {
  const mode = useMode();
  const prompt = ref('');
  const result = ref('');
  const isLoading = ref(false);

  const { typedOutput, animateTyping } = useTypewriter();

  const click = async () => {
    if (!prompt.value.trim()) return;
    isLoading.value = true;
    result.value = '';
    typedOutput.value = '';

    try {
      const response = await fetch(
        `https://hype-machine-ud8o.onrender.com/${mode.value}?prompt=${encodeURIComponent(
          prompt.value,
        )}`,
      );
      console.log(response);
      const data = await response.json();
      console.log(data);
      const output = data.message || data.hype || data.melody || data.error || 'No response.';
      result.value = output;
      animateTyping(output);
    } catch (error) {
      console.error(error);
      result.value = 'Something went wrong.';
      typedOutput.value = result.value;
    } finally {
      isLoading.value = false;
    }
  };

  return {
    prompt,
    result,
    isLoading,
    click,
  };
};
