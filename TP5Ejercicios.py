#Ejercicio 1
notas = [2, 3, 4, 5, 6, 7, 8, 9, 10]

contador= 0
for _ in notas: 
    contador += 1
promedio = sum(notas) / contador

print ("notas: ", notas)
print ("promedio: ", promedio)
print ("nota mas alta: ", max(notas), "nota mas baja: ", min(notas))

#Ejercicio 2

productos = []
for i in range (5):
    producto = input(f"ingrese un producto: ")
    productos.append (producto)
print("lista ordenada: ", sorted (productos))

eliminar = input ("Que producto deseas eliminar: ")
if eliminar in productos:
    productos.remove (eliminar)
print (" lista actulizada: ", sorted(productos))

#Ejercicio 3
import random 
numeros = [random. randint (1, 100) for _ in range (15)]
print ("lista completa: " numeros)

pares = []
impares = []
 for numero in numeros:
     if numero % 2 == 0:
        pares.append(numero)
    else:
        impares.append(numero)
print ("lista de numeros pares: ", pares)
print ("cantidad de numero pares: ", len (pares))

#Ejercicio 4
datos = [1, 3, 5, 3, 7, 1, 9, 5, 3]

repetir=[]
for numero in datos:
    if numero not in repetir:
        repetir.append(numero)
print("numeros sin repetir ", repetir)

#Ejercicio 5
estudiantes = ["Arturo", "Olga", "Ana", "Mirta", "Sofia", "Azul", "Carlos", "Luis"]
print("Lista de estudiantes:", estudiantes)

accion = input("¿Quiere agregar un nuevo estudiante o eliminar uno existente? ")

if accion == "agregar":
    nuevo = input("Ingrese el nombre del nuevo estudiante: ")
    estudiantes.append(nuevo)

elif accion == "eliminar":
    eliminar = input("Ingrese el nombre del estudiante a eliminar: ")
    if eliminar in estudiantes:
        estudiantes.remove(eliminar)
    else:
        print("El estudiante no está en la lista")
print("Lista actualizada:", estudiantes)

#Ejercicio 6 
numeros = [1, 2, 3, 4, 5, 6, 7]

numero1 = [numeros[-1]]   
numero2 = numeros[:-1]   
rotacion = numero1 + numero2
print(rotacion)

#Ejercicio 7
temperatura = [
    [18, 19],
    [20, 21],
    [22, 23],
    [24, 25],
    [11, 12],
    [10, 15],
    [26, 27]
]

minima = [dia[0] for dia in temperatura]
maxima = [dia[1] for dia in temperatura]

temp_min = sum(minima) / len(minima)
temp_max = sum(maxima) / len(maxima)

print("Promedio de temperatura mínima:", temp_min)
print("Promedio de temperatura máxima:", temp_max)
amplitudes = [dia[1] - dia[0] for dia in temperatura]
mayor_amplitud = max(amplitudes)
dia = amplitudes.index(mayor_amplitud) + 1

print("Mayor amplitud:", mayor_amplitud, "°C")
print("Día con mayor amplitud:", dia)

#Ejercicio 8

notas = [
    [7, 8, 9],   
    [6, 5, 8],   
    [9, 7, 6],  
    [8, 8, 10], 
    [5, 6, 7]    
]

print("Notas:")

for fila in notas:
    for nota in fila:
        print(nota, end=".")  
    print() 

#Ejercicio 9

