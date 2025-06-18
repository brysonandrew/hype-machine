
export const useMode = () => {
  const mode = useState<THypeMode>('mode', () => 'trash-talk');

  return mode;
};
