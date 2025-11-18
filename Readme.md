📌 Práctica 03 — Validación del Software con Pruebas Automatizadas

Este proyecto corresponde a la Práctica 03 de la asignatura Gestión de la Calidad de Software, Plataformas y Aplicaciones, en la carrera de Negocios Digitales.
Su propósito es implementar procesamiento de datos tributarios del SRI y validarlo mediante pruebas unitarias escritas en Python usando el módulo unittest.

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

🎯 Objetivo

Implementar funciones de análisis tributario usando Python y validarlas con pruebas automatizadas que garanticen su precisión, coherencia y comportamiento correcto frente a errores.

🛠️ Tecnologías Utilizadas

Python 3.10+

Editor: Visual Studio Code

Librerías estándar:

csv

unittest

Librería de cobertura de código:

coverage

📄 Descripción del Proyecto

El programa analiza información del archivo sri_ventas_2024.csv, el cual contiene datos tributarios como ventas, compras, exportaciones e importaciones por provincia.

Se implementa una clase Analizador con funciones de procesamiento:

✔ Funciones principales

ventas_totales_por_provincia()
Retorna un diccionario con el total de ventas agrupado por provincia.

ventas_por_provincia(nombre)
Retorna el total de ventas para una provincia específica.

✔ Entrada principal del programa

En app.py, se muestran:

Totales por provincia

Consulta interactiva de una provincia ingresada por teclado

🧪 Pruebas Unitarias

Las pruebas en tests/test_analizador.py validan:

Que la función retorne un diccionario.

Que los valores sean numéricos y no negativos.

Que exista coherencia en la cantidad de provincias.

Que las provincias consultadas existan.

Validación explícita de 3 provincias con valores esperados.

📊 Estadísticas adicionales implementadas (Trabajo autónomo)

(Selecciona según lo que hayas implementado)

Ejemplo:

Provincia con mayor volumen de importaciones

Porcentaje de ventas con tarifa 0% respecto al total por provincia

Exportaciones totales por mes

Incluye pruebas unitarias para validar los cálculos adicionales.

📈 Cobertura de Código

Para medir la cobertura del proyecto:

1. Instalar Coverage
pip install coverage

2. Ejecutar las pruebas
coverage run -m unittest discover

3. Generar el reporte
coverage report -m

4. (Opcional) Generar un reporte HTML
coverage html


Se creará una carpeta /htmlcov que podrás abrir en tu navegador.

Incluye aquí tu porcentaje real de cobertura.
Ejemplo:

Cobertura total del proyecto: 87%

▶️ Ejecución del Programa
python app.py


Salida esperada:

Listado de ventas totales por provincia

Solicitud de ingreso de una provincia

Resultado de ventas de la provincia consultada

📸 Evidencias

Incluye en tu repositorio:

Captura de salida de la ejecución de app.py

Captura de ejecución de pruebas unitarias

Captura del reporte de cobertura

✔ Conclusiones

Se comprendió el uso del módulo unittest para validar funciones de forma automática.

Se reforzó la importancia de diseñar casos de prueba para asegurar confiabilidad del software.

Se aplicó análisis real sobre datos tributarios del SRI.

Se utilizó correctamente la herramienta coverage para medir calidad del código.

📚 Referencias

Python unittest documentation

SRI Dataset — Ventas y Compras

Video tutoriales y documentación adicional sobre pruebas automatizadas en Python