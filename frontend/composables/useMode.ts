
export const useMode = () => {
  const mode = useState<THypeMode>('mode', () => 'promote');

  return mode;
};
