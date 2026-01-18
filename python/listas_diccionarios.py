# =========================
# LISTAS Y DICCIONARIOS
# =========================

# 1. Lista simple
nombres = ["Juan","Ana","Pedro","Maria","Gaviria"]

print("Lista de nombres:")
for nombre in nombres:
    print(nombre)

print("----")

# 2. Diccionario simple
persona = {
    "nombre": "Juan",
    "edad": 30,
    "ciudad": "Medellín",

    "nombre":"Gaviria",
    "edad":51,
    "ciudad":"Medellin"
}

print("Datos de persona:")
print("Nombre:", persona["nombre"])
print("Edad:", persona["edad"])
print("Ciudad:", persona["ciudad"])

print("----")


# 3. Lista de diccionarios (MUY IMPORTANTE)
personas = [
    {"nombre": "Juan", "valor": 100},
    {"nombre": "Ana", "valor": 200},
    {"nombre": "Pedro", "valor": 150},
    {"nombre": "Maria", "valor": 300},
    {"nombre":"Gaviria","valor":1000}
]

print("Listado de personas y valores:")
for p in personas:
    print(p["nombre"], "→", p["valor"])

"""Las listas guardan colecciones
Los diccionarios dan significado
Una lista de diccionarios representa datos tabulares
Aquí nace el análisis de datos
"""
