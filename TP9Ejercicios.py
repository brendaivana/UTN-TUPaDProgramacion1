# Ejercicio 1
def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n - 1)

num = int(input("ingrese el numero:  "))

for i in range(1, num + 1):
    print(f"Factorial de {i} = {factorial(i)}")
    
# Ejercecio 2
def fibonacci(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)

num = int(input("ingresar posición para Fibonacci "))

print("Serie completa:")
for i in range(num + 1):
    print(fibonacci(i), end=" ")
    
#Ejercicio 3
def potencia(base, exponente):
    if exponente == 0:
        return 1
    return base * potencia(base, exponente - 1)
print(potencia(3, 6))

#Ejercicio 4 
def decimal_a_binario(n):
    binario = {0: "0", 1: "1"}
    if n < 2:
        return binario[n]
    return decimal_a_binario(n // 2) + binario[n % 2]
numero = int(input("Ingrese un número en decimal: "))
resultado = decimal_a_binario(numero)
print(f"El número {numero} en binario es: {resultado}")

#Ejercicio 5
def es_palindromo(palabra):
    if len(palabra) <= 1:
        return True 
    if palabra[0] != palabra[-1]:
        return False
    return es_palindromo(palabra[1:-1])


palabra = input("ingrese una palabra:  ").lower()

if es_palindromo(palabra):
    print("Es un palíndromo")
else:
    print("No es un palíndromo")

#Ejercicio 6
def suma_digitos(n):
    if n < 10:
        return n   
    ultimo = n % 10
    resto = n // 10
    return ultimo + suma_digitos(resto)

numero = int(input("Ingresa un número: "))
print("La suma de los dígitos es:", suma_digitos(numero))

#Ejercicio 7
def contar_bloques(n):
    if n == 1:
        return 1
    return n + contar_bloques(n - 1)
numero = int(input("cantidad de bloques más bajo: "))
print("total de bloques ", contar_bloques(numero))

#Ejercicio 8
def contar_digito(numero, digito):
    if numero == 0:
        return 0
    ultimo = numero % 10
    if ultimo == digito:
        return 1 + contar_digito(numero // 10, digito)
    else:
        return contar_digito(numero // 10, digito)

num = int(input("ingrese un numero: "))
d = int(input("ingresar el digito que queres contar(0-9): "))
print("Aparece", contar_digito(num, d), "veces")


