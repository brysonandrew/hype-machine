import { ref } from 'vue';
import { useTypewriter } from './useTypewriter';

export const useHypeClick = () => {
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
      // const response = await fetch(`/hype?prompt=${encodeURIComponent(prompt.value)}`);
      const response = await fetch(`/api`);
      console.log(response);
      const data = await response.json();
      console.log(data);
      const output = data.hype || data.melody || data.error || 'No response.';
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
    typedOutput,
    click,
  };
};
