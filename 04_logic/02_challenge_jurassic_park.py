"""
En Jurassic Park, se ha observado que los dinosaurios carnívoros, como el temible T-Rex, depositan un número par de huevos. 
Imagina que tienes una lista de números enteros en la que cada número representa la cantidad de huevos puestos por un dinosaurio en el parque.

Importante: Solo se consideran los huevos de los dinosaurios carnívoros (T-Rex) aquellos números que son pares.

Objetivo:
Escribe una función en Python que reciba una lista de números enteros y devuelva la suma total de los huevos que pertenecen a los dinosaurios carnívoros 
(es decir, la suma de todos los números pares en la lista).
"""

from os import system
if system("clear") != 0: system("cls")

# Para ver si un número es par
# siempre usamos el módulo %
# nos da el resto de la división: eggs % 2 == 2

def suma_huevo_trex(lista_huevos) -> int:
    suma_total = 0
    for huevo in lista_huevos:
        if huevo % 2 == 0:  # Verifica si el número es par
            suma_total = suma_total + huevo
    return suma_total

    # mas corta y eficiente usando filter y sum
    # suma_total = sum(filter(lambda x: x % 2 == 0, lista_huevos))

    # return suma_total

print(suma_huevo_trex([1, 2, 3, 4, 5, 6]))  # Salida: 12
print(suma_huevo_trex([10, 15, 20, 25, 30]))  # Salida: 60
