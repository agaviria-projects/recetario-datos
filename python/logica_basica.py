# =========================
# LÓGICA BÁSICA EN PYTHON
# =========================

# 1. Variables
a = 2
b = 5

print("Valor de a:",a)
print("Valor de b",b)

#2. Condicional
if a > b:
    print("a es mayor que b")
else:
    print("b es mayor que a")

#3. Bucle
for i in range(3):
    print("Iteración:",i)

#4. Función
def sumar(x,y):
    return x + y
    
resultado =sumar(2,3)
print("Resultado de la suma:", resultado)

"""
Lógica básica – Python

- Un programa fluye de arriba hacia abajo
- Las variables controlan el comportamiento
- Los if deciden caminos
- Los for repiten
- Las funciones encapsulan lógica

Problema:
Entender cómo fluye un programa de inicio a fin.

Cuándo usar:
Siempre antes de trabajar con datos, SQL o Power BI.

Patrón mental:
Variables → Condición → Bucle → Función

Error típico:
Copiar código sin modificar valores.

"""

