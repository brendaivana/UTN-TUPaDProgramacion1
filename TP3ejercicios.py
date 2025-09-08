#Ejercicio 1
edad = int(input("Ingrese su edad: "))
if edad >= 18:
    print("Es mayor de edad")
    
    
#Ejercicio 2
nota = int(input("Ingrese su nota: "))
if nota >= 6:
    print("Aprobado")
else:
    print("Desaprobado")

#Ejercicio 3
numero = int(input("Ingrese un número: "))
if numero % 2 == 0:
    print("Ha ingresado un número par")
else:
    print("Por favor, ingrese un número par")
    
#Ejercicio 4 
edad = int(input("Ingrese su edad: "))
if edad < 12:
    print("Niño/a")
elif edad < 18:  
    print("Adolescente")
elif edad < 30:  
    print("Adulto/a joven")
else:
    print("Adulto/a")
    
#Ejercicio 5
contraseña = input("Ingrese una contraseña: ")
if 8 <= len(contraseña) <= 14:
    print("Ha ingresado una contraseña correcta")
else:
    print("Por favor, ingrese una contraseña de entre 8 y 14 caracteres")
    
#Ejercicio 6
# import random
# numeros_aleatorios = [random.randint(1, 100) for i in range(50)]

# media = mean(numeros_aleatorios)
# mediana = median(numeros_aleatorios)
# moda = mode(numeros_aleatorios)

#Ejercicio 7
texto = input("Ingrese una frase o palabra: ")
if texto[-1].lower() in "a e i o u":
    texto = texto + "!"
    
print(texto)

#Ejercicio 8 
nombre = input("Ingrese su nombre: ")
opcion = input("Ingrese 1 (mayusculas)2 (minusculas) 3 (primera letra mayusculas):")
if opcion == "1":
    nombre = nombre.upper()
elif opcion == "2":
    nombre = nombre.lower()
elif opcion == "3":
    nombre = nombre.title()
else:
    print("Opción inválida.")
    
print("Resultado:", nombre)

#Ejercicio 9 
magnitud = float(input("Ingrese la magnitud del terremoto: "))

if magnitud < 3:
    print("Muy leve (imperceptible)")
elif magnitud < 4:  
    print("Leve (ligeramente perceptible)")
elif magnitud < 5: 
    print("Moderado (sentido por personas pero generalmente no causa daños)")
elif magnitud < 6:  
    print("Fuerte (puede causar daños en estructuras debiles)")
elif magnitud < 7: 
    print("Muy Fuerte (puede causar daños significativos)")
else: 
    print("Extremo (puede causar graves daños a gran escala)")
    
#Ejercicio 10 