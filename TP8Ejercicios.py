# Ejercicio 1
def crear_archivo():
    with open("productos.txt", "w", encoding="utf-8") as archivo:
        archivo.write("Leche,1500,10\n")
        archivo.write("Fideos,950,25\n")
        archivo.write("Harina,1000,15\n")
    print("Archivo 'productos.txt' creado con 3 productos iniciales.")

# Ejercicio 2
def leer_y_mostrar():
    print("\nLISTA DE PRODUCTOS")
    with open("productos.txt", "r", encoding="utf-8") as archivo:
        for linea in archivo:
            nombre, precio, cantidad = linea.strip().split(",")
            print(f"Producto: {nombre} | Precio: ${precio} | Cantidad: {cantidad}")

# Ejercicio 3
def agregar_producto_archivo():
    print("\n--- AGREGAR PRODUCTO ---")
    nombre = input("Nombre del producto: ").strip()
    precio = input("Precio: ").strip()
    cantidad = input("Cantidad: ").strip()

    with open("productos.txt", "a", encoding="utf-8") as archivo:
        archivo.write(f"{nombre},{precio},{cantidad}\n")

    print("Producto agregado correctamente al archivo.")

# Ejercicio 4
def cargar_productos():
    productos = []
    with open("productos.txt", "r", encoding="utf-8") as archivo:
        for linea in archivo:
            nombre, precio, cantidad = linea.strip().split(",")
            productos.append({
                "nombre": nombre,
                "precio": float(precio),
                "cantidad": int(cantidad)
            })
    return productos

# Ejercicio 5
def buscar_producto(productos):
    buscado = input("\nIngrese el nombre del producto a buscar: ").strip().lower()

    for p in productos:
        if p["nombre"].lower() == buscado:
            print(f"Encontrado → Nombre: {p['nombre']} | Precio: ${p['precio']} | Cantidad: {p['cantidad']}")
            return

    print("Producto no encontrado.")

# Ejercicio 6
def guardar_actualizado(productos):
    with open("productos.txt", "w", encoding="utf-8") as archivo:
        for p in productos:
            archivo.write(f"{p['nombre']},{p['precio']},{p['cantidad']}\n")
    print("\nArchivo actualizado correctamente.")

def main():
    crear_archivo()
    leer_y_mostrar()
    agregar_producto_archivo()

    productos = cargar_productos()
    buscar_producto(productos)

    guardar_actualizado(productos)

main()
