import json

# -------------------------
# CLASES
# -------------------------

class Usuario:
    def __init__(self, nombre, email):
        self.nombre = nombre
        self.email = email

    def mostrar_info(self):
        return f"{self.nombre} - {self.email}"


# HERENCIA Y POLIMORFISMO
class Cliente(Usuario):
    def __init__(self, nombre, email, direccion):
        super().__init__(nombre, email)
        self.direccion = direccion

    def mostrar_info(self):
        return f"Cliente: {self.nombre} - {self.direccion}"


class Producto:
    def __init__(self, id, nombre, marca, talla, precio, stock):
        self.id = id
        self.nombre = nombre
        self.marca = marca
        self.talla = talla
        self.precio = precio
        self.stock = stock

    def mostrar_info(self):
        return f"{self.id}. {self.nombre} - ${self.precio}"

    def reducir_stock(self):
        self.stock -= 1


class Carrito:
    def __init__(self):
        self.productos = []

    def agregar_producto(self, producto):
        if producto.stock > 0:
            self.productos.append(producto)
            producto.reducir_stock()
            print("Producto agregado")
        else:
            print("Sin stock")

    def mostrar_carrito(self):
        print("\\nCARRITO")

        for producto in self.productos:
            print(producto.mostrar_info())

    def calcular_total(self):
        return sum(p.precio for p in self.productos)


class Pedido:
    def __init__(self, cliente, productos):
        self.cliente = cliente
        self.productos = productos
        self.total = sum(p.precio for p in productos)

    def mostrar_resumen(self):
        print("\\nPEDIDO")
        print(self.cliente.mostrar_info())

        for producto in self.productos:
            print(producto.mostrar_info())

        print("Total:", self.total)


class Pago:
    def __init__(self, metodo, monto):
        self.metodo = metodo
        self.monto = monto

    def procesar(self):
        print(f"Pago realizado con {self.metodo} por ${self.monto}")


class Envio:
    def __init__(self, direccion, tipo):
        self.direccion = direccion
        self.tipo = tipo

    def calcular_costo(self):
        if self.tipo == "express":
            return 20000
        return 10000


class Tienda:
    def __init__(self):
        self.productos = []

    def agregar_producto(self, producto):
        self.productos.append(producto)

    def mostrar_productos(self):
        print("\\nPRODUCTOS")

        for producto in self.productos:
            print(producto.mostrar_info())


# -------------------------
# MANEJO DE ARCHIVOS
# -------------------------

ARCHIVO = "productos.json"


def guardar_productos(productos):
    datos = []

    for p in productos:
        datos.append({
            "id": p.id,
            "nombre": p.nombre,
            "marca": p.marca,
            "talla": p.talla,
            "precio": p.precio,
            "stock": p.stock
        })

    with open(ARCHIVO, "w") as archivo:
        json.dump(datos, archivo, indent=4)


# -------------------------
# MAIN
# -------------------------

tienda = Tienda()

p1 = Producto(1, "Air Jordan 1", "Nike", 42, 500000, 5)
p2 = Producto(2, "Yeezy 350", "Adidas", 41, 700000, 3)

tienda.agregar_producto(p1)
tienda.agregar_producto(p2)

guardar_productos(tienda.productos)

cliente = Cliente(
    "Daniel",
    "nietodaniel365@gmail.com",
    "Barranquilla"
)

carrito = Carrito()

while True:
    print("\\n--- MENU ---")
    print("1. Ver productos")
    print("2. Agregar producto")
    print("3. Ver carrito")
    print("4. Comprar")
    print("5. Salir")

    opcion = input("Seleccione: ")

    if opcion == "1":
        tienda.mostrar_productos()

    elif opcion == "2":
        id_producto = int(input("ID del producto: "))

        for producto in tienda.productos:
            if producto.id == id_producto:
                carrito.agregar_producto(producto)

    elif opcion == "3":
        carrito.mostrar_carrito()

    elif opcion == "4":
        pedido = Pedido(cliente, carrito.productos)
        pedido.mostrar_resumen()

        pago = Pago("Tarjeta", pedido.total)
        pago.procesar()

        envio = Envio(cliente.direccion, "express")
        costo = envio.calcular_costo()

        print("Costo envio:", costo)
        print("Total final:", pedido.total + costo)

    elif opcion == "5":
        print("Programa finalizado")
        break

    else:
        print("Opcion invalida")
