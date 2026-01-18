# =========================
# MANEJO DE ERRORES
# =========================

datos = [
    {"nombre": "Juan", "valor": 100},
    {"nombre": "Ana", "valor": "200"},
    {"nombre": "Pedro", "valor": None},
    {"nombre": "Maria", "valor": 300},
    {"nombre": "Error", "valor": "abc"},
    {"nombre": "Error", "valor": ""}
]

for registro in datos:
    try:
        nombre = registro["nombre"]
        valor = int(registro["valor"])

        print(nombre, "→", valor)

    except ValueError:
        print("Error de conversión en registro:", registro)

    except TypeError:
        print("Valor nulo o tipo incorrecto en registro:", registro)

"""
Los datos no son confiables
El código debe defenderse
Los errores no son excepciones, son la norma
Un script bueno continúa, no se cae
try / except es una herramienta de negocio, no académica

Esto explica directamente por qué proyectos como control_ans_v5:
tienen muchos try
tienen muchos if
parecen “largos”
👉 No es complejidad innecesaria.
👉 Es robustez.

No memorices el código.
Recuerda esto:
Siempre validar antes de convertir
Nunca confiar en los datos
Siempre capturar errores críticos
Un script que se cae = problema en producción
"""