###
# exercises.py
# Ejercicios para practicar los conceptos aprendidos en las lecciones.
###

from os import system
if system("clear") != 0: system("cls")

print("\nEjercicio 1: Imprimir mensajes")
print("Escribe un programa que imprima tu nombre y tu ciudad en líneas separadas.")

### Completa aquí

print("Mi nombre es Ricardo")
print("y vivo en Quilpue")

print("--------------")

print("\nEjercicio 2: Muestra los tipos de datos de las siguientes variables:")
print("Usa el comando 'type()' para determinar el tipo de datos de cada variable.")
a = 15
b = 3.14159
c = "Hola mundo"
d = True
e = None

### Completa aquí

print(type(a))
print(type(b))
print(type(c))
print(type(d))
print(type(e))
print("")
print("--------------")

print("\nEjercicio 3: Casting de tipos")
print("Convierte la cadena \"12345\" a un entero y luego a un float.")
print("Convierte el float 3.99 a un entero. ¿Qué ocurre?")

### Completa aquí

numero_cadena = "12345"
numero_entero = int(numero_cadena)
numero_float = float(numero_entero)
print("Número entero:", numero_entero)
print("Número como float:", numero_float)

print("")
numero_decimal = 3.99
numero_cambiado = int(numero_decimal)  # Se trunca el decimal
print("Float original:", numero_decimal)
print("Float convertido a entero (se trunca la parte decimal):", numero_cambiado)
print("")
print("--------------")

print("\nEjercicio 4: Variables")
print("Crea variables para tu nombre, edad y altura.")
print("Usa f-strings para imprimir una presentación.")

nombre = "Ricardo"
edad = 26
altura = 1.86

print(f"Hola, mi nombre es {nombre}, tengo {edad} años y mido {altura} metros.")
print("")
print("--------------")

print("\nEjercicio 5: Números")
print("1. Crea una variable con el número PI (sin asignar una variable)")
print("2. Redondea el número con round()")
print("3. Haz la división entera entre el número que te salió y el número 2")
print("4. El resultado debería ser 1")

pi = 3.14159
print(round(pi))  # Redondea el número PI
print("el resultado es ", round(pi) // 2)  # División entera entre el número redondeado y 2
