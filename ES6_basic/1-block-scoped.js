export default function taskBlock(trueOrFalse) {
  const task = false;
  const task2 = true;

  if (trueOrFalse) {
    // Suppression des déclarations redondantes pour éviter les erreurs.
    // Les variables task et task2 dans le bloc if étaient locales et non liées
    // aux variables extérieures. Pour modifier les variables extérieures,
    // il faudrait les manipuler directement sans les redéclarer.
    // Cependant, étant déclarées avec `const`, elles ne peuvent être réassignées.
    // Ainsi, ce bloc est laissé vide ou supprimé, car il ne peut fonctionner
    // comme initialement prévu en respectant les règles ESLint.
  }

  return [task, task2];
}
