listaProductos = []
cuentaProductos = []

print("Bienvenido al cajero de Tzuzul Code con python!")
agregarProductos = input("Quiere agregar productos?")

def informacionProducto():
    producto = input("Ingrese nombre de producto")
    productoPrecio = float(input("Ingrese precio de producto"))
    productoStock = int(input("Ingrese cantidad de producto"))
    productoFinal = [producto, productoPrecio, productoStock]
    listaProductos.extend([productoFinal])

def mostrarProductos(lista, mensaje):
    contador = 0
    if(len(lista)>0):
        print(mensaje)
        for i in lista:
            print(f"{contador} - {i[0]}")
            contador += 1
        contador = 0
    else:
        print("No hay mas productos en la tienda")

def totalCuenta():
    sumaTotal = 0
    for i in cuentaProductos:
        sumaTotal += i[1]
    print(f"Tu total es de ${sumaTotal}. Gracias por tu compra!")   

def eliminarProductos(lista, mensaje):
    eliminarProductos = input("Quiere eliminar productos?")
    while(eliminarProductos == "si" and len(lista) > 0):
        mostrarProductos(lista, mensaje)
        eliminarId = int(input("Ingrese el numero del producto que quiere eliminar"))
        del lista[eliminarId]
        mostrarProductos(lista, mensaje)
        if (len(lista) > 0):
            eliminarProductos = input("Quiere eliminar productos?")

def gestionarCuenta():
    if (len(listaProductos) > 0):
        agregarMasProductos = input("Quiere agregar productos a su cuenta?")
        while(agregarMasProductos == "si" or agregarMasProductos == "Si" and len(listaProductos) > 0):
            if(len(listaProductos) > 0):
                mostrarProductos(listaProductos, "Productos en tienda")
                agregarACuentaDeProductos = int(input("Ingrese el numero del producto que quiere agregar a su cuenta"))
                if(listaProductos[agregarACuentaDeProductos][2] > 0 ):
                    productoFinal = [listaProductos[agregarACuentaDeProductos][0], listaProductos[agregarACuentaDeProductos][1]]
                    cuentaProductos.extend([productoFinal])
                    print(f"Agregaste {listaProductos[agregarACuentaDeProductos][0]} a tu cuenta")
                    listaProductos[agregarACuentaDeProductos][2] -= 1
                    print(cuentaProductos)
                    agregarMasProductos = input("Quiere agregar mas productos a su cuenta?")
                else:
                    print("Ya no quedan unidades")
                    del listaProductos[agregarACuentaDeProductos]
                    agregarMasProductos = input("Quiere agregar mas productos a su cuenta?")
            if(agregarMasProductos == "no" or len(listaProductos) == 0):
                if(len(listaProductos) == 0 and len(cuentaProductos) > 0):
                    print("Ya no quedan mas productos para agregar a su cuenta.")
                    eliminarProductos(cuentaProductos, "Productos en su cuenta")
                    totalCuenta()
                    break
                else:
                    mostrarProductos(cuentaProductos, "Productos en su cuenta")
                    eliminarProductos(cuentaProductos, "Productos en su cuenta")
                    totalCuenta()
                    break
        if(len(cuentaProductos) == 0 and agregarMasProductos != "si"):
            print("No agregaste ningun producto a tu cuenta.")                          

if(agregarProductos == "si" or agregarProductos == "Si"):
    while(agregarProductos == "si" or agregarProductos == "Si"):
        informacionProducto()
        agregarProductos = input("Quiere agregar productos?")
        if (agregarProductos != "si" or agregarProductos == "Si"):
            eliminarProductos(listaProductos, "Productos en tienda")
else:
    print("Adios!")

gestionarCuenta()
