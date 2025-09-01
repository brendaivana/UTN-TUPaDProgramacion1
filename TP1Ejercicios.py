#Ejercicio 1
print("Hola mundo!!") 

#Ejercicio 2
nombre = input("Ingrese su nombre ")

print(f"Hola {nombre}!")

#Ejercicio 3
nombre = input("Ingrese su nombre: ")
apellido = input("Ingrese su apellido: ")
edad = input("Ingrese su edad: ")
residencia = input("Ingrese su lugar de residencia: ")

print(f"Hola, Soy {nombre} {apellido} tengo {edad} años y vivo en {residencia}")

#Ejercicio 4
pi = 3.1416
radio = float(input("Ingresa el radio del circulo: "))
area = pi * radio * 2
perimetro = 2 * pi * radio

print(f"el area del circulo es: {area}")
print(f"el perimetro del circulo es: {perimetro}")

#Ejercicio 5
segundos = int(input("ingrese los segundos: "))
horas = segundos / 3600

print(f"{segundos} son {horas} horas")

#Ejercicio 6
numero = int(input("ingrese un numero: "))

print(numero, "x 1 =", numero * 1)
print(numero, "x 2 =", numero * 2)
print(numero, "x 3 =", numero * 3)
print(numero, "x 4 =", numero * 4)
print(numero, "x 5 =", numero * 5)
print(numero, "x 6 =", numero * 6)
print(numero, "x 7 =", numero * 7)
print(numero, "x 8 =", numero * 8)
print(numero, "x 9 =", numero * 9)
print(numero, "x 10 =", numero * 10)

#Ejercicio 7
numero1 = int(input("Ingresa un numero que no sea 0: "))
numero2 = int(input("Ingresa otro numero que no sea 0: "))

print(f"El resultado de la suma es: {numero1 + numero2}")
print(f"El resultado de la resta es: {numero1 - numero2}")
print(f"El resultado de la multiplicacion es: {numero1 * numero2}")
print(f"El resultado de la division es: {numero1 / numero2}")

#Ejercicio 8
peso = int(input("ingresa tu peso: "))
altura = int(input("ingresa tu altura: "))

imc = peso / altura ** 2

print (" el indice de masa corporal es: ", imc )

#Ejercicio 9
celsius = int(input("Ingresa una temperatura en grados celsius: "))
fahrenheit = (9 / 5) * celsius + 32

print (f"{celsius}el equivalente en grados Fahrenheit es:  {fahrenheit}")

#Ejercicio 10
numero1 = int(input("ingresa el primer numero: "))
numero2 = int (input("ingresa el segundo numero: "))
numero3 = int(input("ingresa el tercer numero: "))

promedio = (numero1 + numero2 + numero3) / 3
print ("el promedio es: ", promedio)