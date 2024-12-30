from colorama import init, Fore, Back,Style

init()

opcion = None
Contador_id = 1

def cargar_nuevo_modelo():
    Marca = input("Ingresa la Marca \n")
    Modelo = input("Ingresa el Modelo \n")
    Kilometraje = input("Ingresa Kilometraje \n")
    Color = input("Ingresa el color \n")
    stock = int(input("Ingresa el stock \n"))  

    global Contador_id
    Contador_id += 1
    Modelos_Stock[Contador_id] = {
        "Marca": Marca,
        "Modelo": Modelo,
        "Kilometraje": Kilometraje,
        "Color": Color,
        "stock": stock
    }

def Mostrar_Motos():
    if not Modelos_Stock:
        print(Fore.RED+Back.BLACK+Style.BRIGHT+"No hay motos en el stock."+Style.RESET_ALL)
        return

    for id, moto in Modelos_Stock.items():
        print(f"  {'🏍️ ' * 20}\n id: {id}- Modelo: {moto['Modelo']} - Kilometraje: {moto['Kilometraje']} - Color: {moto['Color']} - stock: {moto['stock']}")
    
def Editar_stock_motos():
    print("🏍️ " * 20)
    print("Editando Modelos..... ")
    print("Modelos Disponibles : ")
    Mostrar_Motos()

    id_a_Modificar = int(input(" Ingrese el id del modelo a modificar: "))

    if id_a_Modificar not in Modelos_Stock:
        print(Fore.RED+Back.BLACK+Style.BRIGHT+"Id no encontrado"+Style.RESET_ALL)
        return

    Modelo_a_editar = Modelos_Stock[id_a_Modificar]
    Nuevo_stock = int(input("Ingrese nuevo stock: "))
    Modelo_a_editar["stock"] = Nuevo_stock

def Eliminar_Moto():
    print("Eliminando Modelo....")
    Mostrar_Motos()
    id_a_borrar = int(input("Ingrese el id a Borrar: "))

    if id_a_borrar not in Modelos_Stock:
        print(Fore.RED+Back.BLACK+Style.BRIGHT+"Id no encontrado"+Style.RESET_ALL)
        return

    del Modelos_Stock [id_a_borrar]

def Buscar_Moto_por_Modelo():
   print("buscando producto....")
   nombre_a_buscar = input("Ingrese el nombre a buscar: ")
    
   productos_encontrados = {}
    
   for id, modelo in Modelos_Stock.items():
       
       if nombre_a_buscar.lower() in modelo["Modelo"].lower(): 
           productos_encontrados[id] = modelo
    
   if len(productos_encontrados) == 0:
        print(Fore.RED+Back.BLACK+Style.BRIGHT+"No encontramos el Modelo"+Style.RESET_ALL)
        return
   else:
       
       for id, modelo in productos_encontrados.items():
           print("🏍️ " * 20)
           print(f"id: {id}-")
           print(f"Modelo: {moto['Modelo']}")
           print(f"Kilometraje: {moto['Kilometraje']}")
           print(f"Color: {moto['Color']}")
           print(f"stock: {moto['stock']}")

def Reporte_bajo_stock():
   print("Reporte de bajo stock.....\n")
   cantidad_bajo_stock = int(input("Indica la cantidad para evaluar el stock : "))

   productos_bajo_stock = {}

   for id,modelo in Modelos_Stock.items():
     if modelo["stock"] <= cantidad_bajo_stock:
        productos_bajo_stock[id] = modelo
    
   if len(productos_bajo_stock)==0:
    print(Fore.RED+Back.BLACK+Style.BRIGHT+"No hay Modelos con bajo stock"+Style.RESET_ALL)
    return

   for id, moto in productos_bajo_stock.items():
           print("🏍️ " * 20)
           print(f"id: {id}-")
           print(f"Modelo: {moto['Modelo']}")
           print(f"Kilometraje: {moto['Kilometraje']}")
           print(f"Color: {moto['Color']}")
           print(f"stock: {moto['stock']}")

def enter_para_continuar():
    input("Presiona Enter para continuar....")

Modelos_Stock = {
    1: {"Marca": "CF Motos", "Modelo": "300 nk", "Kilometraje": 2500, "Color": "Azul", "stock": 5}
}

print(Fore.LIGHTWHITE_EX+Back.RED+Style.BRIGHT + "🏍️🏍️🏍️***CONSECIONARIO DE MOTOS USADAS***🏍️🏍️🏍️ "+ Style.RESET_ALL)

while True:
    print("🏍️ " * 20)
    print(Fore.BLUE+ " 1...Agregar Datos📄 \n 2...Mostrar Listas📖 \n 3...Editar Stock✏️ \n 4...Elimina Modelo❌ \n 5...Buscar Modelo🔎\n 6...Reporte bajo Stock⚠️\n 0...Salir📤 "+ Style.RESET_ALL)
    opcion = input(Fore.YELLOW+Back.BLACK+Style.BRIGHT +"ingresa una opcion: "+Style.RESET_ALL)

    if opcion == "1":
        cargar_nuevo_modelo()
    elif opcion == "2":
        Mostrar_Motos()
    elif opcion == "3":
        Editar_stock_motos()
    elif opcion == "4":
        Eliminar_Moto()
    elif opcion == "5":
        Buscar_Moto_por_Modelo()
    elif opcion=="6":
        Reporte_bajo_stock()
    elif opcion == "0":
        print("Saliste del Menu \n")
        break  # Salimos del bucle
    else:
        print("🏍️ " * 20)
        print("ingresa una opcion valida \n")

    enter_para_continuar()
