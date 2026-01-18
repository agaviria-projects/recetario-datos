# =========================
# LECTURA DE ARCHIVOS
# =========================

ruta_archivo ="datos.txt"

with open(ruta_archivo,"r",encoding="utf-8")as archivo:
    for linea in archivo:
        linea=linea.strip()
        nombre,valor=linea.split(",")
        valor=int(valor)

        print("Nombre",nombre)
        print("Valor",valor)
        print("----")

"""
¿Por qué Python?

“Porque es muy fuerte para automatización y manejo de datos, 
permite leer archivos, validar información y escalar el proceso
fácilmente.”

Construí un script en Python que lee archivos de texto, procesa cada registro, 
valida el formato y convierte los datos para que puedan ser analizados.
El enfoque fue modular y orientado a evitar errores comunes como rutas
incorrectas o datos mal formateados.”

Lectura de archivos – Python

Problema:
Los datos vienen desde archivos externos.

Cuándo usar:
Cuando recibes TXT o CSV sin estructura avanzada.

Patrón mental:
Archivo → línea → separación → conversión.

Error típico:
Rutas incorrectas o datos mal formateados.

Cuando un senior abre un proyecto de miles de líneas:
❌ No lee todo
❌ No memoriza
❌ No recorre archivo por archivo

Hace esto:
Entiende qué problema resuelve el sistema
Identifica bloques funcionales
Aprende puntos de entrada
Ubica dónde tocar cuando hay un cambio
Ignora el resto hasta que sea necesario

Analogía simple (para que quede claro)
Proyecto grande = ciudad
No te aprendes todas las calles

Aprendes:
avenidas principales
zonas
puntos clave
El resto lo miras solo cuando necesitas ir ahí.
"""

