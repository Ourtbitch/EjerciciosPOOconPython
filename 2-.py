#Ejercicio 2: Sistema de Gestión de Pedidos
#Desarrolla un sistema de gestión de pedidos utilizando herencia múltiple y MRO.

#Clase base: Producto

#Atributos: nombre, precio
#Método: mostrar_informacion

#Clase derivada: Electrodomestico (hereda de Producto)
#Atributos adicionales: marca, garantia_anios
#Métodos adicionales: tiene_garantia

#Clase derivada: Ropa (hereda de Producto)
#Atributos adicionales: talla, material
#Métodos adicionales: es_material_sintetico

#Clase derivada: Alimento (hereda de Producto)
#Atributos adicionales: fecha_caducidad, es_organico
#Métodos adicionales: es_caducado

#Implementa un sistema donde puedas gestionar productos, verificar garantías, tipos de material y estado de caducidad.
import datetime
class Producto:
    def __init__(self, nombre, precio):
        self.nombre = nombre
        self.precio = precio

    def mostrar_informacion(self):
        return f"Nombre: {self.nombre}\nPrecio: S/.{self.precio}"


class Electrodomestico(Producto):
    def __init__(self, nombre, precio, marca, garantia_anios):
        super().__init__(nombre, precio)
        self.marca = marca
        self.garantia_anios = garantia_anios

    def tiene_garantia(self):
        return self.garantia_anios >= 1


class Ropa(Producto):
    def __init__(self, nombre, precio, talla, material):
        super().__init__(nombre, precio)
        self.talla = talla
        self.material = material

    def es_material_sintetico(self):
        return self.material.lower() == "sintetico"


class Alimento(Producto):
    def __init__(self, nombre, precio, fecha_caducidad, es_organico):
        super().__init__(nombre, precio)
        self.fecha_caducidad = fecha_caducidad
        self.es_organico = es_organico

    def es_caducado(self):
        import datetime
        return self.fecha_caducidad < datetime.date.today()


class Tienda:
    def __init__(self):
        self.lista = []

    def agregar_producto(self, producto):
        self.lista.append(producto)

    def mostrar_todos(self):
        for producto in self.lista:
            print(producto.mostrar_informacion())
            if isinstance(producto, Electrodomestico):
                print(f"Marca: {producto.marca}")
                print(f"Tiene garantía: {'Sí' if producto.tiene_garantia() else 'No'}")
            elif isinstance(producto, Ropa):
                print(f"Talla: {producto.talla}")
                print(f"Material: {producto.material}")
                print(f"Es material sintético: {'Sí' if producto.es_material_sintetico() else 'No'}")
            elif isinstance(producto, Alimento):
                print(f"Fecha de caducidad: {producto.fecha_caducidad}")
                print(f"Es orgánico: {'Sí' if producto.es_organico else 'No'}")
                print(f"Está caducado: {'Sí' if producto.es_caducado() else 'No'}")
            print("\n")


tienda = Tienda()

n = 0
while n != 4:
    n = int(input("\nBienvenido al menú de opciones:\n1-Agregar Electrodoméstico\n2-Agregar Ropa\n3-Agregar Alimento\n4-Salir\n"))
    if n == 1:
        nombre = input("Nombre: ")
        precio = float(input("Precio: "))
        marca = input("Marca: ")
        garantia_anios = int(input("Años de garantía: "))
        electrodomestico = Electrodomestico(nombre, precio, marca, garantia_anios)
        tienda.agregar_producto(electrodomestico)
    elif n == 2:
        nombre = input("Nombre: ")
        precio = float(input("Precio: "))
        talla = input("Talla: ")
        material = input("Material: ")
        ropa = Ropa(nombre, precio, talla, material)
        tienda.agregar_producto(ropa)
    elif n == 3:
        nombre = input("Nombre: ")
        precio = float(input("Precio: "))
        fecha_caducidad = input("Fecha de caducidad (YYYY-MM-DD): ")
        es_organico = input("Es orgánico (sí/no): ").lower() == 'sí'
        alimento = Alimento(nombre, precio, datetime.date.fromisoformat(fecha_caducidad), es_organico)
        tienda.agregar_producto(alimento)
    elif n == 4:
        tienda.mostrar_todos()