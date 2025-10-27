#Ejercicio 1

# def imprimir_hola_mundo():
#     print("Hola mundo")
# imprimir_hola_mundo()

#Ejercicio 2

# def saludar_usuario(nombre):
#     return f"Hola {nombre}!"
# nombre_usuario = input("ingrese su nombre: ")
# print(saludar_usuario(nombre_usuario))

#Ejercicio 3

# def informacion_personal(nombre, apellido, edad, residencia):
#     print(f"Soy {nombre} {apellido}, tengo {edad} años y vivo en {residencia}.")
# nombre_usuario = input("ingrese su nombre: ")
# apellido_usuario = input("ingrese su apellido: ")
# edad_usuario = input("ingrese su edad: ")
# residencia_usuario = input("¿donde vivis?: ")

# informacion_personal(nombre_usuario, apellido_usuario, edad_usuario, residencia_usuario)

#Ejercicio 4

# import math

# def calcular_area_circulo(radio):
#     area = math.pi * (radio ** 2)
#     return area
# def calcular_perimetro_circulo(radio):
#     perimetro = 2 * math.pi * radio
#     return perimetro
# radio = float(input("Ingresá el radio del círculo: "))
# area = calcular_area_circulo(radio)
# perimetro = calcular_perimetro_circulo(radio)

# print(f"El área del círculo es: {area:.2f}")
# print(f"El perímetro del círculo es: {perimetro:.2f}")

#Ejercicio 5

# def segundos_a_horas(segundos):
#     horas = segundos / 3600
#     return horas
# seg = float(input("Ingresá la cantidad de segundos: "))
# resultado = segundos_a_horas(seg)

# print(f"{seg} segundos equivalen a {resultado:.2f} horas ")

#Ejercicio 6

# def tabla_multiplicar(numero):
#     print(f"Tabla de multiplicar del {numero}:")
#     for i in range(1, 11):
#         print(f"{numero} x {i} = {numero * i}")
# num = int(input("Ingresá un número para ver su tabla de multiplicar: "))
# tabla_multiplicar(num)

#Ejercicio 7

# def operaciones_basicas(a, b):
#     suma = a + b
#     resta = a - b
#     multiplicacion = a * b
#     division = a / b if b != 0 else "No se puede dividir entre 0"
#     return (suma, resta, multiplicacion, division)

# a = float(input("ingresa el primer numero: "))
# b = float(input("ingresa el segundo numero: "))

# resultados = operaciones_basicas(a, b)

# print(f"Suma: {resultados[0]}")
# print(f"Resta: {resultados[1]}")
# print(f"Multiplicación: {resultados[2]}")
# print(f"División: {resultados[3]}")


#Ejercicio 8

# def calcular_imc(peso, altura):
#     imc = peso / (altura ** 2)
#     return imc
# peso = float(input("ingresa tu peso en kilogramos: "))
# altura = float(input("ingresa tu altura en metros: "))

# resultado = calcular_imc(peso, altura)

# print(f"Tu índice de masa corporal (IMC) es: {resultado:.2f}")

#Ejercicio 9

# def celsius_a_fahrenheit(celsius):
#     fahrenheit = (celsius * 9/5) + 32
#     return fahrenheit
# celsius = float(input("ingresa la temperatura en grados celsius: "))
# resultado = celsius_a_fahrenheit(celsius)
# print(f"{celsius}°C equivalen a {resultado:.2f}°F")

#Ejercicio 10

def calcular_promedio(a, b, c):
    promedio = (a + b + c) / 3
    return promedio
a = float(input("ingresa el primer numero: "))
b = float(input("ingresa el segundo numero: "))
c = float(input("ingresa el tercer numero: "))

resultado = calcular_promedio(a, b, c)

print(f"el promedio de los tres números es: {resultado:.2f}")

