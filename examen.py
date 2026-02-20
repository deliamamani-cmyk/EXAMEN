# primer examen

# Clase Producto
class Producto:
    def __init__(self, nombre, precio, cantidad):  
        self.nombre = nombre
        self.precio = precio
        self.cantidad = cantidad

    def mostrar_info(self):
        print("Nombre:", self.nombre)
        print("Precio:", self.precio)
        print("Cantidad:", self.cantidad)
        print("Valor total:", self.valor_total())
        print("---------")

    def valor_total(self):
        return self.precio * self.cantidad


# Lista vacía
productos = []


# Función para agregar producto
def agregar_producto():
    nombre = input("Ingrese nombre del producto: ")
    precio = float(input("Ingrese precio: "))
    cantidad = int(input("Ingrese cantidad: "))

    nuevo_producto = Producto(nombre, precio, cantidad)
    productos.append(nuevo_producto)

    print("Producto agregado correctamente.\n")


# Función para mostrar productos
def mostrar_productos(): 
    if len(productos) == 0:
        print("No hay productos registrados.\n")
    else:
        for producto in productos:
            producto.mostrar_info()


# Menú interactivo
while True:
    print("===== MENU =====")
    print("1. Agregar producto")
    print("2. Mostrar productos")
    print("3. Salir")

    opcion = input("Seleccione una opcion: ")

    if opcion == "1":
        agregar_producto()
    elif opcion == "2":
        mostrar_productos()
    elif opcion == "3":
        print("Saliendo del programa.")
        break
    else:
        print("Opcion invalida. Intente nuevamente.\n")
