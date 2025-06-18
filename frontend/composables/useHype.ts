import { ref } from 'vue';
import { useTypewriter } from './useTypewriter';

export const useHype = () => {
  const mode = useMode();
  const target = ref('');
  const context = ref('');
  const result = ref('');
  const isLoading = ref(false);

  const { typedOutput, animateTyping } = useTypewriter();

  const click = async () => {
    isLoading.value = true;
    result.value = '';
    typedOutput.value = '';

    try {
      const params = { target: target.value, context: context.value };
      const queryString = new URLSearchParams(params).toString();

      const response = await fetch(`${API_URL}/${mode.value}?${queryString}`);
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
    context,
    target,
    result,
    isLoading,
    click,
  };
};
