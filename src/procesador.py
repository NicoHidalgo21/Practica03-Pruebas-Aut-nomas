import csv

class Analizador:
    def __init__(self, ruta_csv):
        # Guardamos la ruta del archivo CSV
        self.ruta_csv = ruta_csv
        # Leemos el archivo CSV y guardamos los datos en memoria
        self.datos = self.leer_csv()

    def leer_csv(self):
        """Lee el archivo CSV y devuelve una lista de filas."""
        datos = []
        try:
            with open(self.ruta_csv, "r", encoding="utf-8") as archivo:
                # Usamos el delimitador '|'
                lector = csv.DictReader(archivo, delimiter='|')
                for fila in lector:
                    datos.append(fila)
            return datos
        except FileNotFoundError:
            print(f"Error: El archivo {self.ruta_csv} no fue encontrado.")
            return []

    def provincias_unicas(self):
        """
        Devuelve un conjunto (set) de todas las provincias únicas, normalizadas a minúsculas.
        Esto se usa para la validación de la entrada del usuario.
        """
        return {fila["PROVINCIA"].lower() for fila in self.datos}

    def ventas_totales_por_provincia(self):
        """
        Devuelve un diccionario con el total de ventas por provincia.
        Las claves están en minúsculas.
        """
        totales = {}
        for fila in self.datos:
            provincia = fila["PROVINCIA"].lower()
            try:
                total_venta = float(fila["TOTAL_VENTAS"])
                totales[provincia] = totales.get(provincia, 0.0) + total_venta
            except (ValueError, KeyError):
                continue
        return totales

    def ventas_por_provincia(self, nombre):
        """
        Devuelve el total de ventas de una provincia específica.
        Si no existe, devuelve 0.0.
        """
        totales = self.ventas_totales_por_provincia()
        return totales.get(nombre.lower(), 0.0)

    # ===============================================================
    # NUEVA FUNCIÓN 1: EXPORTACIONES TOTALES POR MES
    # ===============================================================
    def exportaciones_totales_por_mes(self):
        """
        Suma las exportaciones totales agrupadas por MES.
        Devuelve un diccionario: {mes: total_exportaciones}
        """
        totales = {}
        for fila in self.datos:
            try:
                mes = fila["MES"]
                valor = float(fila["EXPORTACIONES"])
                totales[mes] = totales.get(mes, 0) + valor
            except (KeyError, ValueError):
                continue
        return totales

    # ===============================================================
    # NUEVA FUNCIÓN 2: PROVINCIA CON MAYOR IMPORTACIÓN
    # ===============================================================
    def provincia_mayor_importacion(self):
        """
        Devuelve la provincia que tiene el mayor total de IMPORTACIONES.
        Las claves se normalizan a minúsculas.
        """
        totales = {}
        for fila in self.datos:
            try:
                provincia = fila["PROVINCIA"].lower()
                valor = float(fila["IMPORTACIONES"])
                totales[provincia] = totales.get(provincia, 0) + valor
            except (KeyError, ValueError):
                continue

        if not totales:
            raise ValueError("No existen datos válidos de importaciones.")

        # Devuelve la provincia con mayor valor
        return max(totales, key=totales.get)
