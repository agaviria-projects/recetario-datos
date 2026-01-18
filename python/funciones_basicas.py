# =========================
# FUNCIONES REUTILIZABLES
# =========================

def sumar(a,b):
    return a + b

def restar(a,b):
    return a - b

def multiplicar(a,b):
    return a * b

def dividir(a,b):
    if b == 0:
        return None
    return a / b

print("Suma:", sumar(2, 5))
print("Resta:", restar(5, 5))
print("Multiplicación:", multiplicar(0, 5))
print("División:", dividir(3, 5))
print("División por cero:", dividir(10, 3))

"""
Una función recibe datos (parámetros)
Procesa lógica
Devuelve un resultado (return)
Puede protegerse contra errores
Se puede reutilizar infinitas veces
"""
