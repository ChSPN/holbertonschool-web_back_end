function getStudentsByLocation(students, city) {
  return students.filter((student) => student.location === city);
}

// Exemple d'utilisation de la fonction pour éviter l'erreur "no-unused-vars"
console.log(getStudentsByLocation([{ id: 1, firstName: 'Guillaume', location: 'San Francisco' }], 'San Francisco'));
