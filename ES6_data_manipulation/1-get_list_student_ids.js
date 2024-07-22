function getListStudentIds(array) {
  if (!Array.isArray(array)) {
    return [];
  }
  return array.map((student) => student.id);
}

// Exemple d'utilisation de la fonction pour éviter l'erreur "no-unused-vars"
console.log(getListStudentIds([{ id: 1 }, { id: 2 }, { id: 3 }]));
