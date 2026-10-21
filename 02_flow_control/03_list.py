###
# 03 - Listas
# Secuencias mutables de elementos.
# Pueden contener elementos de diferentes tipos.
###

import os
os.system("cls")  # Limpiar la consola (en Windows)

# Creación de listas
print("\nCrear listas")
lista1 = [1, 2, 3, 4, 5] # lista de enteros
lista2 = ["manzanas", "peras", "plátanos"] # lista de cadenas de texto
lista3 = [1, "hola", 3.14, True] # lista de tipos mixtos

lista_vacia = [] # lista vacía
lista_de_listas = [[1, 2], ["calcetín", 4]] # lista de listas o matriz
matriz = [[1, 2, 3], [4, 5, 6]] # matriz o lista de listas

print(lista1)
print(lista2)
print(lista3)
print(lista_vacia)
print(lista_de_listas)
print(matriz)

# Acceso a elementos por índice
print("\nAcceso a elementos por índice")
print(lista2[0])  # manzanas
print(lista2[1])  # peras
print(lista2[-1]) # plátanos
print(lista2[-2]) # peras

print(lista_de_listas[1][0]) # calcetín

# Slicing (rebanado) de listas
lista1 = [1, 2, 3, 4, 5]
print(lista1[1:4]) # [2, 3, 4]
print(lista1[:3])  # [1, 2, 3]
print(lista1[3:])  # [4, 5]
print(lista1[:])   # [1, 2, 3, 4, 5] Copia
print("--------------")

# El tercer parámetro es el paso (step)
lista1 = [1, 2, 3, 4, 5, 6, 7, 8]
print(lista1[::2]) # para devolver índices pares
print(lista1[::-1]) # para devolver índices inversos

# Modificar elementos de una lista
lista1[0] = 10
print(lista1)  # [10, 2, 3, 4, 5]

# Agregar elementos a una lista
lista1 = [1, 2, 3]

# Forma mas larga y menos eficiente de agregar elementos a una lista
lista1 = lista1 + [4, 5]
print(lista1)

# Forma mas corta y eficiente de agregar elementos a una lista
lista1 += [6, 7, 8 ,9]
print(lista1)

lista_letras = ["a", "b", "c"]
# Recuperar longitud de una lista
print("Longitud de la lista", len(lista1)) # 9
print("Longitud de la lista", len(lista_letras)) # 3

###
# EJERCICIOS
###

# Ejercicio 1: El mensaje secreto
# Dada la siguiente lista:
# mensaje = ["C", "o", "d", "i", "g", "o", " ", "s", "e", "c", "r", "e", "t", "o"]
# Utilizando slicing y concatenación, crea una nueva lista que contenga solo el mensaje "secreto".

mensaje = ["C", "o", "d", "i", "g", "o", " ", "s", "e", "c", "r", "e", "t", "o"]
secreto = mensaje[7:]
print(secreto)

# Ejercicio 2: Intercambio de posiciones
# Dada la siguiente lista:
# numeros = [10, 20, 30, 40, 50]
# Intercambia la primera y la última posición utilizando solo asignación por índice.

# numeros = [10, 20, 30, 40, 50]
# numeros[0] = 50
# numeros[4] = 10
# print(numeros)

numeros = [10, 20, 30, 40, 50]
numeros[0], numeros[-1] = numeros[-1], numeros[0] # Intercambio en una sola línea.
print(numeros)

# Ejercicio 3: El sándwich de listas
# Dadas las siguientes listas:
# pan = ["pan arriba"]
# ingredientes = ["jamón", "queso", "tomate"]
# pan_abajo = ["pan abajo"]
# Crea una lista llamada sandwich que contenga el pan de arriba, los ingredientes y el pan de abajo, en ese orden.

pan = ["pan arriba"]
ingredientes = ["jamón", "queso", "tomate"]
pan_abajo = ["pan abajo"]

sandwich = pan + ingredientes + pan_abajo
print(sandwich)

# Ejercicio 4: Duplicando la lista
# Dada una lista:
# lista = [1, 2, 3]
# Crea una nueva lista que contenga los elementos de la lista original duplicados.
# Ejemplo: [1, 2, 3] -> [1, 2, 3, 1, 2, 3]

lista = [1, 2, 3]
nueva_lista = lista + lista
print(nueva_lista)

# Ejercicio 5: Extrayendo el centro
# Dada una lista con un número impar de elementos, extrae el elemento que se encuentra en el centro de la lista utilizando slicing.
# Ejemplo: lista = [10, 20, 30, 40, 50] -> El centro es 30

lista = [10, 20, 30, 40, 50, 60, 70]
centro = len(lista) // 2
print(lista[centro])

# Ejercicio 6: Reversa parcial
# Dada una lista, invierte solo la primera mitad de la lista (utilizando slicing y concatenación).
# Ejemplo: lista = [1, 2, 3, 4, 5, 6] -> Resultado: [3, 2, 1, 4, 5, 6]

lista = [1, 2, 3, 4, 5, 6]
mitad = len(lista) // 2
listainvertida = lista[:mitad][::-1] + lista[mitad:]
print(listainvertida)

# lista_inver = lista[:mitad][::-1] + lista[mitad:][::-1]
# print(lista_inver)