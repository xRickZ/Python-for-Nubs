from os import system
if system("clear") != 0: system("cls")


def battle(lista_a, lista_b):
    puntos_a = 0
    puntos_b = 0
    for index in range(len(lista_a)):
        if lista_a[index] > lista_b[index]:
            puntos_a += 1
        elif lista_b[index] > lista_a[index]:
            puntos_b += 1
        # else: empate, no se suma nada
    if puntos_a > puntos_b:
        return "a"
    elif puntos_b > puntos_a:
        return "b"
    else:
        return "x"
    
lista_a = [3, 8, 4, 1]
lista_b = [2, 2, 4, 3]

winner = battle(lista_a, lista_b)
print(winner)



# Ejercicio 1. Contar números pares
# Crea una función contar_pares(lista) que reciba una lista y devuelva cuántos números pares contiene.
print("\n Ejercicio 1. Contar números pares")
def contar_pares(lista):
    numero = 0
    for recorriendo_nums in lista:
        if recorriendo_nums % 2 == 0:
            numero += 1
    return numero

lista = [1, 2, 3, 4, 5, 6]
print(contar_pares(lista))

print("\n Ejercicio 2. Encontrar el numero más grande")
#Crea una función encontrar_mayor(lista) que devuelva el número más grande de una lista no vacía, sin utilizar max()

def encontrar_mayor(lista):
    mayor = lista[0]  # Inicializamos con el primer elemento de la lista
    for numero in lista:
        if numero >= mayor:
            mayor = numero
    return mayor

lista = [7, 2, 3, 4, 5, 6]
print(encontrar_mayor(lista))

print("\n Ejercicio 3. Sumar solo los positivos")
# Crea una función sumar_positivos(lista) que sume únicamente los números mayores que cero.

def sumar_positivos(lista):
    suma = 0
    for numero in lista:
        if numero > 0:
            suma += numero
    return suma

lista = [1, -2, 3, -4, 5]
print(sumar_positivos(lista))

print("\n Ejercicio 4. Marcador de dos jugadores")
# Crea una función marcador(jugador_a, jugador_b) que compare dos listas de igual longitud. 
# Cada posición representa una ronda: el número mayor gana un punto y los empates no suman puntos.

# Devuelve "a" si A gana más rondas, "b" si B gana más o "x" si empatan.

def marcador(jugador_a, jugador_b):
    puntos_a = 0
    puntos_b = 0
    for index in range(len(jugador_a)):
        if jugador_a[index] > jugador_b[index]:
            puntos_a += 1
        elif jugador_b[index] > jugador_a[index]:
            puntos_b += 1
    if puntos_a > puntos_b:
        return f"{puntos_a}a"
    elif puntos_b > puntos_a:
        return f"{puntos_b}b"
    else:
        return "x"
    
print(marcador([8, 3, 7], [4, 9, 2]))

print("\n Ejercicio 5. Buscar un número")
# Crea una función buscar_numero(lista, objetivo) que devuelva True si el número está en la lista y False si no está. No utilices in.

def buscar_numero(lista, objetivo):
    for numero in lista:
        if numero == objetivo:
            return True
    return False
print(buscar_numero([3, 6, 9, 12], 9))

print("\n Ejercicio 6. Contar números negativos")
# Crea una función contar_negativos(lista) que devuelva cuántos números menores que cero hay.

def contar_negativos(lista):
    contador = 0
    for numero in lista:
        if numero < 0:
            contador += 1
    return contador
print(contar_negativos([4, -2, -7, 0, 5, -1]))


print("\n Ejercicio 7. Promedio de una lista ")
# Crea una función calcular_promedio(lista) que devuelva el promedio de sus números. Puedes suponer que la lista no está vacía.
      
def calcular_promedio(lista):
    suma_notas = 0
    for notas in lista:
        suma_notas += notas
    return suma_notas / len(lista)

print(calcular_promedio([4, 6, 8, 10]))

print("\n Ejercicio 8. Contar cuántas veces aparece un número")
# Crea una función contar_apariciones(lista, objetivo) que devuelva cuántas veces aparece el objetivo.

def contar_apariciones(lista, objetivo):
    guardado = 0
    for numeros in lista:
        if numeros == objetivo:
            guardado += 1
    return guardado

print(contar_apariciones([2, 5, 2, 8, 2, 5], 2))
# Resultado: 3

print("\n Ejercicio 9. Invertir una lista")
# Crea una función invertir_lista(lista) que devuelva una lista con los elementos en orden inverso.

def invertir_lista(lista):
    num_inver = []
    for numeros in range(len(lista)-1, -1, -1):
        numeros = num_inver.append(lista[numeros])
    return num_inver

print(invertir_lista([1, 2, 3, 4, 5]))

print("\n Ejercicio 10. Comparar dos listas")
# Crea una función comparar_listas(lista_a, lista_b) que compare los números de ambas 
# listas en cada posición y devuelva cuántas rondas termina ganando A.

# El empate no suma puntos y puedes suponer que ambas listas tienen el mismo largo.

def comparar_listas(lista_a, lista_b):
    numeros_a = 0
    numeros_b = 0
    for index in range(len(lista_a)):
        if lista_a[index] > lista_b[index]:
            numeros_a += 1
        elif lista_b[index] > lista_a[index]:
            numeros_b += 1
    if numeros_a > numeros_b:
        return numeros_a
    elif numeros_a < numeros_b:
        return numeros_b
    else:
        return "empate"

print(comparar_listas([5, 8, 3, 7], [2, 9, 3, 4]))
# Resultado: 2
