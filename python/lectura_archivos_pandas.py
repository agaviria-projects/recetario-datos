# =========================
# LECTURA DE ARCHIVOS CON PANDAS
# =========================

import pandas as pd

# Leer archivo CSV
ruta_csv = "ventas.csv"
df = pd.read_csv(ruta_csv)

print("Datos cargados desde CSV:")
print(df)

print("\nInformación del DataFrame:")
print(df.info())

print("\nFiltrar valores mayores a 200:")
print(df[df["valor"] > 200])

"""
Lectura de archivos con pandas

Problema:
Los datos vienen desde archivos externos (CSV/Excel).

Cuándo usar:
Cuando recibes datos de sistemas, proveedores o reportes.

Patrón mental:
Archivo → DataFrame → validación → análisis.

Errores típicos:
- Ruta incorrecta
- Nombres de columnas distintos
- Tipos de datos mal inferidos
"""
"""
El análisis empieza con read_csv
df.info() es tu primera auditoría
Los filtros validan hipótesis
Si los datos cargan bien → el resto fluye
"""