#Repositorio Calculadora-git
Bienvenidos a la Calculadora-git!
Este programa hace la función de una calculadora, puede hacer:

-Sumatorias.
-Restas.
-Multiplicación.
-División.


Pipeline de CI/CD:

GitHub Actions: Build and Package
Este pipeline de GitHub Actions está configurado para automatizar el proceso de construcción, pruebas y empaquetado de la aplicación Python. Se ejecuta en un entorno Ubuntu y sigue los siguientes pasos:

-Checkout del código: Clona el repositorio en el entorno de ejecución.
-Configuración de Python: Establece Python 3.12 como la versión a utilizar.
-Instalación de dependencias: Instala las dependencias necesarias..
-Instalación de herramientas de construcción: Instala setuptools y wheel para el empaquetado.
-Ejecución de pruebas: Ejecuta pruebas automáticas usando pytest.
-Empaquetado de la aplicación: Construye los archivos de distribución (sdist y bdist_wheel) usando setup.py.
-Carga del paquete como artefacto: Sube el paquete generado como un artefacto para su descarga posterior.