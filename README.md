#Repositorio Calculadora-git
Bienvenidos a la Calculadora-git!
Este programa hace la función de una calculadora, puede hacer:

-Sumatorias.
-Restas.
-Multiplicación.
-División.


Pipeline de CI/CD:

Este pipeline de GitHub Actions está configurado para ejecutar pruebas automáticas en Python cada vez que se realice un push o se cree un pull request a la rama uat. Los pasos principales incluyen:

-Checkout del código: Clona el repositorio.
-Configuración de Python: Establece el entorno con Python 3.9.
-Instalación de dependencias: Actualiza pip e instala los -paquetes necesarios desde requirements.txt.
-Ejecución de pruebas: Ejecuta las pruebas con pytest.