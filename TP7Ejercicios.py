# Ejercicio 1
# precios_frutas = {'Banana': 1200, 'Ananá': 2500, 'Melón': 3000, 'Uva': 1450}

# precios_frutas["Naranja"] = 1200
# precios_frutas["Manzana"] = 1500
# precios_frutas["Pera"] = 2300

# print(precios_frutas)

#Ejercicio 2
# precios_frutas['Banana'] = 1330
# precios_frutas['Manzana'] = 1700
# precios_frutas['Melón'] = 2800

# print(precios_frutas)

#Ejercicio 3
# frutas = list(precios_frutas.keys())
# print(frutas)

#Ejercicio 4
# contactos = {
#     "juan": "113456",
#     "ana": "4567"
# }
# for i in range(2): 
#     nombre = input("Ingrese el nombre del contacto: ")
#     telefono = input("Ingrese el número de teléfono: ")
#     contactos[nombre] = telefono

# buscar = input("Ingrese el nombre de contacto: ")

# if buscar in contactos:
#     print(f"El número de {buscar} es {contactos[buscar]}")
# else:
#     print("ese contacto no esta registrado")


#Ejercicio 5
# frase = input("escribi una frase: ")
# palabras = frase.split()
# palabras_unicas = set(palabras)

# recuento = {}
# for palabra in palabras:
#     if palabra in recuento:
#         recuento[palabra] += 1
#     else:
#         recuento[palabra] = 1
# print("palabras unicas:", palabras_unicas)
# print("recuento:", recuento)

#Ejercicio 6
# alumnos = {
#     "Sofía": (10, 9, 8),
#     "Luis": (6, 7, 7),
#     "Ana": (9, 8, 10)
# }

# for nombre, notas in alumnos.items():
#     promedio = sum(notas) / len(notas)
#     print(nombre, "promedio:", promedio)

#Ejercicio 7

#Ejercicio 8
# Diccionario con productos y su stock
# productos = {
#     "fideos": 20,
#     "harina": 15,
#     "yerba": 10
# }

# nombre = input("ingre el nombre del producto: ")

# if nombre in productos:
#     print("stock de", nombre, ":", productos[nombre])
#     agregar = int(input("cuantos productos queres agregar: "))
#     productos[nombre] += agregar
#     print("nuevo stock de", nombre, ":", productos[nombre])
# else:
#     nuevo_stock = int(input("no hay este producto, podes agregarlo: "))
#     productos[nombre] = nuevo_stock
#     print("producto agregado")

# print("\ntodos los productos:")
# print(productos)

#Ejercicio 9
# agenda = {
#     ("lunes", "10:00"): "reunión",
#     ("martes", "15:00"): "Clase de programación I"
# }

# print("Agenda:")
# for clave, evento in agenda.items():
#     print(clave, evento)

# dia = input("ingrese el dia: ")
# hora = input("ingrese la hora: ")
# evento = input("ingrese el evento: ")

# agenda[(dia, hora)] = evento

# print("\nAgenda actualizada:")
# for clave, evento in agenda.items():
#     print(clave, evento)

#Ejercicio 10
original = {
    "Argentina": "Buenos Aires",
    "Chile": "Santiago",
    "Uruguay": "Montevideo"
}
diferente = {}
for pais, capital in original.items():
    diferente[capital] = pais

print("diccionario original:")
print(original)

print("\nDiccionario diferente:")
print(diferente)
