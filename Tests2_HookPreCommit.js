//Prueba #2 para el hook de pre-commit, en este caso deberia funcionar dado que no incumple las reglas del hook dado que:
//1- Se usa la función flecha '=>' correctamente
//2- Hay punto y coma presente después de cada declaración

const adder = (value1, value2) => {
  return value1 + value2;
};

module.exports = adder;