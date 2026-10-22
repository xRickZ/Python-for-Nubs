###
# 04 - Funciones
# Bloques de código reutilizables y parametrizables para hacer tareas especificas
###

from os import system
if system("clear") != 0: system("cls")

# """ Definición de una función

# def nombre_de_la_funcion(parametro1, parametro2, ...):
#   # docstring
#   # cuerpo de la función
#   return valor_de_retorno # opcional

# """

# # Ejemplo de una función para imprimir algo en consola
def saludar():
  print("¡Hola!")
saludar()

# # Ejemplo de una función con parámetro
def saludar_a(nombre):
  print(f"¡Hola {nombre}!")

saludar_a("midudev")
saludar_a("madeval")
saludar_a("pheralb")
saludar_a("felixicaza")
saludar_a("Carmen Ansio")

# Funciones con más parámetros
def sumar(a, b):
  suma = a + b
  return suma

result = sumar(2, 3)
print(result)