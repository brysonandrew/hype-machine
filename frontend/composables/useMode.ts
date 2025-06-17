export const useMode = () => {
  const mode = useState<'promoter' | 'trash-talker'>('mode', () => 'promoter');

  return mode;
};
