lista_productos = []
cuenta_productos = []

print("Bienvenido al cajero de Tzuzul Code con python!")
agregar_productos = input("Quiere agregar productos?")

def informacion_producto():
    producto = input("Ingrese nombre de producto")
    producto_precio = float(input("Ingrese precio de producto"))
    producto_stock = int(input("Ingrese cantidad de producto"))
    producto_final = [producto, producto_precio, producto_stock]
    lista_productos.extend([producto_final])

def mostrar_productos(lista, mensaje, mensaje2):
    contador = 0
    if(len(lista)>0):
        print(mensaje)
        for i in lista:
            print(f"{contador} - {i[0]}")
            contador += 1
        contador = 0
    else:
        print(mensaje2)

def total_cuenta():
    suma_total = 0
    for i in cuenta_productos:
        suma_total += i[1]
    print("----------------------------------------------")
    print(f"Tu total es de ${suma_total}. Gracias por tu compra!")
    print("----------------------------------------------")   

def eliminar_productos(lista, mensaje, mensaje2):
    eliminar_productos = input("Quiere eliminar productos?")
    while(eliminar_productos == "si" and len(lista) > 0):
        mostrar_productos(lista, mensaje, mensaje2)
        eliminar_id = int(input("Ingrese el numero del producto que quiere eliminar"))
        del lista[eliminar_id]
        mostrar_productos(lista, mensaje, mensaje2)
        if (len(lista) > 0):
            eliminar_productos = input("Quiere eliminar productos?")

def mostrar_eliminar_total_productos():
    mostrar_productos(cuenta_productos, "Productos en su cuenta", "No tienes mas productos en tu cuenta")
    eliminar_productos(cuenta_productos, "Productos en su cuenta", "No tienes mas productos en tu cuenta")
    total_cuenta()

def gestionar_cuenta():
    if (len(lista_productos) > 0):
        agregar_mas_productos = input("Quiere agregar productos a su cuenta?")
        while(agregar_mas_productos == "si" or agregar_mas_productos == "Si" and len(lista_productos) > 0):
            if(len(lista_productos) > 0):
                mostrar_productos(lista_productos, "Productos en tienda", "No hay mas productos en la tienda")
                agregar_a_cuenta_de_productos = int(input("Ingrese el numero del producto que quiere agregar a su cuenta"))
                if(lista_productos[agregar_a_cuenta_de_productos][2] > 0 ):
                    producto_final = [lista_productos[agregar_a_cuenta_de_productos][0], lista_productos[agregar_a_cuenta_de_productos][1]]
                    cuenta_productos.extend([producto_final])
                    print(f"Agregaste {lista_productos[agregar_a_cuenta_de_productos][0]} a tu cuenta")
                    lista_productos[agregar_a_cuenta_de_productos][2] -= 1
                    agregar_mas_productos = input("Quiere agregar mas productos a su cuenta?")
                else:
                    print("Ya no quedan unidades")
                    del lista_productos[agregar_a_cuenta_de_productos]
                    agregar_mas_productos = input("Quiere agregar mas productos a su cuenta?")
            if(agregar_mas_productos == "no" or len(lista_productos) == 0):
                if(len(lista_productos) == 0 and len(cuenta_productos) > 0):
                    print("Ya no quedan mas productos para agregar a su cuenta.")
                    mostrar_eliminar_total_productos()
                    break
                else:
                    mostrar_eliminar_total_productos()
                    break

        if(len(cuenta_productos) == 0 and agregar_mas_productos != "si"):
            print("No agregaste ningun producto a tu cuenta.")                          

if(agregar_productos == "si" or agregar_productos == "Si"):
    while(agregar_productos == "si" or agregar_productos == "Si"):
        informacion_producto()
        agregar_productos = input("Quiere agregar productos?")
        if (agregar_productos != "si" or agregar_productos == "Si"):
            eliminar_productos(lista_productos, "Productos en tienda", "No hay mas productos en la tienda")
else:
    print("Adios!")

gestionar_cuenta()
