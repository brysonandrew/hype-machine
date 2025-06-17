export const useMountedCheck = () => {
  const isMounted = ref(false);

  onMounted(() => {
    isMounted.value = true;
  });

  return isMounted;
};
