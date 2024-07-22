function updateStudentGradeByCity(students, city, newGrades) {
  return students
    .filter((student) => student.location === city)
    .map((student) => {
      const gradeObj = newGrades.find((grade) => grade.studentId === student.id);
      return {
        ...student,
        grade: gradeObj ? gradeObj.grade : 'N/A',
      };
    });
}

// Exemple d'utilisation
const students = [{ id: 1, name: 'Alice', location: 'Paris' }];
const newGrades = [{ studentId: 1, grade: 90 }];
console.log(updateStudentGradeByCity(students, 'Paris', newGrades));

// Ou pour l'exporter
module.exports = updateStudentGradeByCity;
