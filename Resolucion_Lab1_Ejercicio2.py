#diccionario de precios
precios = {
    "manzana": 1.5,
    "banana": 2.0,
    "naranja": 1.0,
    "pera": 1.8
}

# Función para mostrar el precio de un producto
def mostrar_precio(producto):
    if producto in precios:
        print("El precio de", producto, "es:", precios[producto])
    else:
        print("El producto", producto, "no está en el diccionario de precios.")

# Función para agregar un nuevo producto y su precio
def agregar_producto(producto, precio):
    precios[producto] = precio
    print("Producto agregado exitosamente.")

# Función para modificar el precio de un producto existente
def modificar_precio(producto, nuevo_precio):
    if producto in precios:
        precios[producto] = nuevo_precio
        print("Precio de", producto, "modificado exitosamente.")
    else:
        print("El producto", producto, "no está en el diccionario de precios.")

# Función para eliminar un producto del diccionario
def eliminar_producto(producto):
    if producto in precios:
        del precios[producto]
        print("Producto eliminado exitosamente.")
    else:
        print("El producto", producto, "no está en el diccionario de precios.")

# Pruebas
mostrar_precio("banana")
agregar_producto("uva", 3.5)
modificar_precio("manzana", 1.8)
eliminar_producto("naranja")