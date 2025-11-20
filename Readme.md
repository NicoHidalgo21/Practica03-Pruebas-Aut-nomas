🚀 Práctica 03 — Validación del Software con Pruebas Automatizadas

📘 Asignatura: Gestión de la Calidad de Software
🎓 Carrera: Negocios Digitales
🧪 Tema: Pruebas unitarias y análisis de datos tributarios (SRI) en Python

Este proyecto implementa funciones de análisis sobre datos tributarios del SRI y valida su correcto funcionamiento mediante pruebas automatizadas con unittest. Además, se integra la herramienta coverage para evaluar la cobertura de código.

📂 Estructura del Proyecto
laboratorio-3/
├── app.py
├── datos/
│   └── sri_ventas_2024.csv
├── src/
│   └── procesador.py
├── tests/
│   └── test_analizador.py
└── README.md

🎯 Objetivos del Proyecto

✔️ Procesar datos tributarios reales del SRI
✔️ Implementar funciones analíticas con Python
✔️ Validar resultados utilizando pruebas unitarias
✔️ Medir la calidad del software mediante cobertura de código
✔️ Aplicar buenas prácticas de programación y versionado con GitHub

🛠️ Tecnologías y Herramientas
Herramienta	Uso
🐍 Python 3.10+	Procesamiento y pruebas
🎨 Visual Studio Code	Edición del código
🧪 unittest	Pruebas automatizadas
📈 coverage.py	Medición de cobertura
📄 CSV del SRI	Datos reales para análisis
📄 Descripción de la Funcionalidad

La clase Analizador ubicada en src/procesador.py procesa el archivo sri_ventas_2024.csv y permite obtener:

🔹 Funciones Principales
📌 ventas_totales_por_provincia()

Retorna un diccionario con el total de ventas por cada provincia.

📌 ventas_por_provincia(nombre)

Devuelve el total de ventas de la provincia indicada.

▶️ Ejecución del Programa

Para correr la aplicación principal:

python app.py


📤 Salida esperada:

Totales de ventas agrupados por provincia

Solicitud de ingreso de una provincia

Visualización de la venta total de la provincia consultada

🧪 Pruebas Unitarias

Las pruebas están en tests/test_analizador.py y verifican:

✔️ El retorno correcto de estructuras (diccionarios)
✔️ Que los valores sean numéricos y no negativos
✔️ Que el número de provincias sea coherente
✔️ Validación de provincias existentes
✔️ Comparación de valores esperados en 3 provincias

Ejecutar las pruebas:

python -m unittest discover

📊 Estadísticas Adicionales (Trabajo Autónomo)

📌 Puedes modificar esta sección según lo que implementaste

Ejemplos incluidos:

📈 Provincia con mayor volumen de importaciones

🧮 Porcentaje de ventas con tarifa 0% por provincia

🌍 Exportaciones totales agrupadas por mes

Cada una incluye sus respectivas pruebas unitarias.

📈 Cobertura de Código
📥 Instalar Coverage
pip install coverage

🧪 Ejecutar pruebas con cobertura
coverage run -m unittest discover

📊 Ver reporte en consola
coverage report -m

🌐 Generar reporte HTML
coverage html


📌 El reporte se almacenará en:

htmlcov/index.html


Ejemplo de cobertura alcanzada:
🔥 Cobertura total del proyecto: 87%

📸 Evidencias Requeridas

Incluye en tu repositorio:

📷 Captura de ejecución de app.py
📷 Captura de ejecución de pruebas unitarias
📷 Captura del reporte de coverage
📂 Archivos .py funcionales

📝 Conclusiones

🧩 Se dominó el uso del módulo unittest para validar funciones.

🔍 Se comprendió cómo diseñar pruebas coherentes para validar tanto cálculos correctos como entradas no válidas.

📊 Se analizó información tributaria real del SRI.

🛡️ Se midió la calidad del código utilizando la librería coverage.

🚀 Se aplicaron buenas prácticas de desarrollo y versionado con GitHub.



🆕 Actualización del Proyecto 19 de noviembre
✔ Configuración y Activación del Entorno Virtual (venv)

Se creó y activó un entorno virtual para aislar las dependencias del proyecto.

Comandos usados:
python -m venv venv
source venv/Scripts/activate

✔ Instalación de Coverage

Se instaló la herramienta coverage para medir la cobertura del código.

 python3 -m pip install --user coverage

✔ Ejecución de Pruebas con Coverage

Se ejecutaron las pruebas unitarias midiendo la cobertura:

coverage run -m unittest discover -s tests -p "test_*.py"

✔ Generación del Reporte de Cobertura:

Reporte HTML:

coverage html

Esto generó una carpeta llamada htmlcov, en el cual generó el reporte.

📚 Referencias

📘 Python Docs — unittest

🏛️ Servicio de Rentas Internas (SRI) — Datos Ventas/Compras

📗 El Libro de Python — Testing

🎥 DigitalOcean — Unit Test Tutorial

🎬 Ejercicios con unittest — Sergio Infante