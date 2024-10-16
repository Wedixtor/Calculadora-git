// Prueba #1 para el hook de pre-commit, en este caso debería funcionar dado que no incumple las reglas del hook dado que:
// 1- se hace uso adecuado de ';'
// 2- Indentación correcta
// 3- Uso correcto de comillas simples/dobles (según tus reglas de ESLint)

function adder(value1, value2) {
  return value1 + value2; // Usa 2 espacios de indentación
}
module.exports = adder;