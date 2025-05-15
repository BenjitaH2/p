##BOTILLERIA JAPI
keoloko = False
carrito = []

precios = {
    "gaseosa": 1200,
    "encendedor": 500,
    "piscola": 1500,
    "papelillos": 1200,
    "boquillas": 700,
    "chicles": 1000,
    "jugo": 800,
    "snacks": 2000,
    "Marihuana" : 10000,
    "blunt": 2000,
    "cigarrillos": 5000,
    "cerveza": 3000,
    "whisky": 20000,
    "vino": 15000,
    "ron": 12000,
    "vodka": 18000,
}

def mostrar_productos_y_precios():
    print("Productos y Precios:")
    for producto, precio in precios.items():
        print(f"{producto}: {precio}CLP")


def mostrar_menu():
    print("Bienvenido a la Botillería JAPI")
    print("1. Agregar producto")
    print("2. Sacar boleta")
    print("3. Salir")

def sistema():
    op = int(input(""))
    match op:
        case 1:
            while True:
                if keoloko == True:
                    break
                mostrar_productos_y_precios()
                producto = input("ingrese el nombre del producto que desea agregar, o escriba 'salir' para terminar: ")
                if producto.lower() == 'salir':
                    break
                cantidad = int(input("Cuantas unidades desea añadir a su carrito?: "))
                for x, y in precios.items():
                    if x == producto.lower():
                        carrito.append(producto, y*cantidad)
                otro = int(input("desea ingresar otro producto? |(1) SI (2) NO"))
                while True:
                    if otro == 2:
                        keoloko = True
                        break
                    elif otro == 1:
                        break
                    else:
                        print("Error! opcion invalida")
                        otro = int(input("desea ingresar otro producto? |(1) SI (2) NO"))
        case 2:
            print("Su boleta es:")

def mostrar_boleta():
    for i in carrito:
        print(i)


    





        #     print(f"Productos agregados: {carrito}")
        # case 2:
        #     if not carrito:
        #         print("No hay productos en el carrito.")
        #     else:
        #         print("Boleta:")
        #         for producto in carrito:
        #             print(f"- {producto}")
        # case 3:
        #     print("Saliendo de la tienda. ¡Hasta luego!")
        # case _:
        #     print("Opción no válida.")