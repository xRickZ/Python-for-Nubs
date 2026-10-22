from os import system
if system("clear") != 0: system("cls")


# Ejercicio 1: Cuenta atrás
# Imprime los números del 10 al 1 usando un bucle while.
print("\nEjercicio 1:")

numeros = 10
while numeros >= 1:
  print(numeros, end=" ")
  numeros = numeros - 1

# Ejercicio 2: Suma de números pares (while)
# Calcula la suma de los números pares entre 1 y 20 (inclusive) usando un bucle while.
print("\nEjercicio 2:")
numero = 1
suma_pares = 0
while numero <= 20:
  if numero % 2 == 0:
    suma_pares = suma_pares + numero
  numero = numero + 1

print(f"La suma de los números pares hasta 20 es: {suma_pares}")

print("\nEste es con numero impar:")
numero = 1
suma_impares = 0
while numero <= 30:
  if numero % 4 == 0:
    suma_impares = suma_impares + numero
  numero = numero + 1

print(f"La suma de los números impares hasta 30 es: {suma_impares}")

print("\n----------------")

# Ejercicio 3: Factorial de un número
# Pide al usuario que introduzca un número entero positivo.
# Calcula su factorial usando un bucle while.
# El factorial de un número entero positivo es el producto de todos los números del 1 al ese número. Por ejemplo, el factorial de 5
# 5! = 5 x 4 x 3 x 2 x 1 = 120.

print("\nEjercicio 3:")
# numero = int(input("Escribe un número entero positivo: "))

# if numero > 0:
#   factorial = 1
#   contador = 1
#   while contador <= numero:
#       factorial =  factorial * contador
#       contador = contador + 1
#   print(f"El factorial de {numero} es: {factorial}")
# else:
#   print("El número debe ser positivo.")

print("\n----------------")

# Ejercicio 4: Validación de contraseña
# Pide al usuario que introduzca una contraseña.
# La contraseña debe tener al menos 8 caracteres.
# Usa un bucle while para seguir pidiendo la contraseña hasta que cumpla con los requisitos.
# Si la contraseña es válida, imprime "Contraseña válida".
print("\nEjercicio 4:")

# contraseña = input("Introduce una contraseña:")

# while len(contraseña) < 8:
#   print ("La contraseña debe tener al menos 8 caracteres.")
#   contraseña = input("Introduce una contraseña nuevamente:")
# print("Contraseña es válida")

print("\n----------------")

# Ejercicio 5: Tabla de multiplicar
# Pide al usuario que introduzca un número.
# Imprime la tabla de multiplicar de ese número (del 1 al 10) usando un bucle while.
print("\nEjercicio 5:")

# numero = int(input("Introduce un número para ver su tabla de multiplicar:"))
# multiplicador = 1
# while multiplicador <= 10:
#   numero_multiplicado = numero * multiplicador
#   multiplicador = multiplicador + 1
#   print(f"{numero} x {multiplicador - 1} es igual a {numero_multiplicado}")
  
print("\n----------------")

# Ejercicio 6: Números primos hasta N
# Pide al usuario que introduzca un número entero positivo N.
# Imprime todos los números primos menores o iguales que N usando un bucle while.

print("\nEjercicio 6:")
n = int(input("Introduce un número entero positivo N: "))

numero = 2
while numero <= n:
  es_primo = True  # Asumimos que el número es primo hasta que se demuestre lo contrario
  divisor = 2
  while divisor * divisor <= numero:  # Optimizamos: no es necesario probar divisores hasta numero
    if numero % divisor == 0:
      es_primo = False  # Si encontramos un divisor, no es primo
      break  # Salimos del bucle interior
    divisor = divisor + 1
  if es_primo:
    print(numero)

  numero = numero + 1
