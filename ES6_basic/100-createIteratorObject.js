export default function createIteratorObject(report) {
  // Stocker tous les employés de tous les départements dans un tableau unique
  const allEmployees = [];
  for (const department of Object.keys(report.allEmployees)) {
    allEmployees.push(...report.allEmployees[department]);
  }

  // Créer et retourner l'itérateur
  let currentIndex = 0;
  return {
    next() {
      if (currentIndex < allEmployees.length) {
        const value = allEmployees[currentIndex];
        currentIndex += 1;
        return { value, done: false };
      }
      return { done: true };
    },
  };
}
