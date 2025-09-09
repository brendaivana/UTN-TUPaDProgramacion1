# Ejercicio 1
for i in range(101):
    print(i)



# Ejercicio 2
numero = int(input("ingrese un numero entero:"))
if numero < 0:
    numero = numero

contador = 0
while numero > 0:
    numero = numero // 10
contador += 1 
print("el numero tiene", contador, "digitos")



# Ejercicio 3
numero1 = int(input("ingrese un numero: "))
numero2 = int(input("ingrese el segundo numero: "))
suma = 0
if numero1 > numero2:
    numero1, numero2 = numero2, numero1
for i in range(numero1 + 1, numero2):
    suma += i
print("la suma de los numeros" , numero1, "y el",  numero2, "da", suma )



# Ejercicio 4

numero = int(input("ingrese un numero y el 0 para terminar: "))
total = 0
while numero != 0:
    total += numero
    numero = int(input("ingrese otro numero y el 0 para terminar: "))
print ("el total es: ", total)


# Ejercicio 5
numero1 = 4
intentos = 0
numero2 = -1
while numero2 != numero1:
    numero2 = int(input("Adivina el numero correcto, ingresa un numero entre el 0 al 9: "))
    intentos += 1
    if numero2 != numero1:
        print("no es correcto intenta otra vez")
print ("es correcto, lo intentaste ", intentos)


# Ejercicio 6
for i in range(100, 0, -1):
      print (i)


# Ejercicio 7
numero= int(input("ingrese un numero positivo: "))
suma = 0
for i in range( 1, numero + 1):
    suma += i
    print("la suma entre 0 y ", numero, "es ", suma)

    
# Ejercicio 8

numero = 3
pares = 0
impares = 0
negativos = 0
positivos = 0

for i in range(numero):
    numero1 = int(input("ingrese un numero: "))
    if numero1 % 2 == 0:
        pares += 1
    else: 
        impares += 1
    if numero1 > 0:
        positivos += 1
    elif numero1 < 0:
        negativos += 1
        
print("los numeros pares son:", pares)
print("los numeros impares son:", impares)
print("los numeros negativos son:", negativos)
print("los numeros positivos son:", positivos)

# Ejercicio 9
numero = 3
suma = 0
for i in range (numero):
    numero1 = int(input("ingrese un numero: "))
    suma += numero1
media= suma / numero
print ("la media de los numeros ingresados es: ", media)

# Ejercicio 10 

numero= int(input("ingrese un numero: "))
invertido = 0
numero1 = numero

while numero1 > 0:
    numero2 = numero1 % 10
    invertido = invertido * 10 + numero2
    
    numero1 = numero1 // 10 
print("el numero invertido es ", invertido)