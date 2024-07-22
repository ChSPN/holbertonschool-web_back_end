function getStudentIdsSum(students) {
  return students.reduce((acc, student) => acc + student.id, 0);
}

// Exemple d'utilisation de la fonction pour éviter l'erreur "no-unused-vars"
const students = [{ id: 1 }, { id: 2 }, { id: 3 }];
console.log(getStudentIdsSum(students));
