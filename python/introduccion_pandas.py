"""
Introducción a pandas
Antes de empezar, una frase importante:
pandas no reemplaza lo que aprendiste.
pandas lo ordena, lo acelera y lo hace legible.
Si no hubieras hecho los días 1–5, pandas sería confuso.
Ahora te va a parecer lógico.
"""
"""
OBJETIVO DEL DÍA 6
Al finalizar hoy, tú sabrás:
Qué es pandas y para qué sirve
Cargar datos desde archivo
Ver datos como tabla
Entender el DataFrame
Conectar pandas con lo que ya sabes
"""
"""
PASO 1 — Instalar pandas (una sola vez)
pip install pandas
"""
"""
pandas trabaja como una tabla
Las operaciones son vectorizadas
El código es más corto pero no más mágico
Todo lo que hacías antes:
listas
diccionarios
validaciones
ahora tiene forma profesional
Por eso pandas no es un salto, es una evolución.
"""

"""
Recuerda esto:
DataFrame = tabla
Columna = Serie
Filtro = condición lógica
Menos bucles, más expresiones
Con eso puedes volver a usar pandas sin problema.
"""
# =========================
# INTRODUCCIÓN A PANDAS
# =========================

import pandas as pd

# Datos simulados (lista de diccionarios)
datos = [
    {"nombre": "Juan", "valor": 100},
    {"nombre": "Ana", "valor": 200},
    {"nombre": "Pedro", "valor": 150},
    {"nombre": "Maria", "valor": 300},
    {"nombre": "Gaviria", "valor": 3000},
]

# Crear DataFrame
df = pd.DataFrame(datos)

print("DataFrame completo:")
print(df)

print("\nSolo columna 'nombre':")
print(df["nombre"])

print("\nFiltrar valores menores a 300:")
print(df[df["valor"] < 300])

