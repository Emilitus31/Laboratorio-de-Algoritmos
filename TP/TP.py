inventario = []
ventas = []
resenias = []
usuario = 0
aviso = False
avisoResenia = False

while True:
    
    while usuario > 3 or usuario < 1:
        print("BIENVENIDO ")
        print("SELECCIONAR ESTADO DE USUARIO: ")
        print(" ")
        print("1. Administrador ")
        print("2. Cliente ")
        print("3. Apagar sistema")
        print(" ")
        usuario = int(input("Elige una opcion: "))
        
    if usuario == 3:
        break

    if usuario == 1:
    
        while True:
            
            if aviso == True:
                print("Se ha vendido un juego!")
                for i, venta in enumerate(ventas, 1):
                            print("-------------------------")
                            print(f"{i}. juego: {venta['juegoVendido']}")
                            print(f"   Unidades vendidas: {venta['UnidadesVendidas']}")
                            print("-------------------------")
                            
                            buscar_jue = venta['juegoVendido']
                            
                            for juego in inventario:
                                if juego['juego'] == buscar_jue:
                                    if juego['stock'] == 0:
                                        print(f"Te has quedado sin stock de {juego['juego']}")
                                        inventario.remove(juego)
                aviso = False
                input("Pulsa enter... ")
                print(" ")
            
            if avisoResenia == True:
                print("Llego una nueva reseña de un juego!")
                for i, resenia in enumerate(resenias, 1):
                            print("-------------------------")
                            print(f"{i}. juego: {resenia['juegoReseniado']}")
                            print(f"   Valoracion Recomendada: {resenia['Recomendacion']}")
                            print("-------------------------")
                            
                avisoResenia = False
                input("Pulsa enter... ")
                print(" ")
        
            print("\n--- SISTEMA DE GESTIÓN DE EMILITUS'S STORE ---")
            print(" ")
            print("1. Registrar nuevo juego")
            print("2. Mostrar todos los juegos")
            print("3. Buscar juego por nombre")
            print("4. Cambiar precio del juego")
            print("5. Reponer stock")
            print("6. Nueva valoracion")
            print("7. Eliminar juego del inventario")
            print("8. Salir")
            print(" ")
            encontrado = False
    
    
            opcion = input("Elige una opción: ")
            print(" ")
        
            match opcion:
                case "1":
                    nombrePro = input("Nombre del juego: ")
                    try:
                        precio = float(input("Precio: "))
                        stock =  int(input("Stock: "))
                        valoracion = int(input("Valoracion (del 1 al 5): "))
                    except ValueError:
                        print("Precio o stock inválidas. Intenta de nuevo.")
                        continue
    
                    if precio <= 0 or stock <= 0 or valoracion > 5 or valoracion < 1:
                        print("Datos inválidos. Intenta de nuevo.")
                    else:
                        nuevo_juego = {
                            "juego": nombrePro,
                            "precio": precio,
                            "stock": stock,
                            "valoracion": valoracion
                        }
                        inventario.append(nuevo_juego)
                        print(f"juego {nombrePro} registrado con éxito.")
    
                case "2":
                    if not inventario:
                        print("No hay juegos registrados aún.")
                    else:
                        print("\njuegos registrados:")
                        print("-------------------------")
                        for i, juego in enumerate(inventario, 1):
                            print(f"{i}. juego: {juego['juego']}")
                            print(f"   Precio: ${juego['precio']}")
                            print(f"   Stock: {juego['stock']}")
                            print(f"   Valoracion: {juego['valoracion']}★")
                            print("-------------------------")
    
                case "3":
                    if not inventario:
                        print("No hay juegos registrados.")
                    else:
                        buscar_jue = input("Escribe el nombre del juego que quieras buscar: ")
                    
                        for juego in inventario:
                            if juego['juego'] == buscar_jue:
                                print("-------------------------")
                                print(f"   juego: {juego['juego']}")
                                print(f"   Precio: ${juego['precio']}")
                                print(f"   Stock: {juego['stock']}")
                                print(f"   Valoracion: {juego['valoracion']}★")
                                print("-------------------------")
                                encontrado = True
                    
                        if encontrado == False:
                            print("No se encontro ese juego")
                        
                case "4":
                    if not inventario:
                        print("No hay juegos registrados.")
                    else:
                    
                        buscar_jue = input("Escribe el nombre del juego al que quieras cambiar el precio: ")
                    
                        for juego in inventario:
                            if juego['juego'] == buscar_jue:
                                print("-------------------------")
                                print(f"   juego: {juego['juego']}")
                                print(f"   Precio: ${juego['precio']}")
                                print(f"   Stock: {juego['stock']}")
                                print(f"   Valoracion: {juego['valoracion']}★")
                                print("-------------------------")
                                nuevo_precio = float(input("Cual es el nuevo precio? "))
                                if nuevo_precio <= 0:
                                    print("Datos inválidos. Intenta de nuevo.")
                                else:
                                    juego['precio'] = nuevo_precio
                                    print("Nuevo precio: ")
                                    print(f"   Precio: {juego['precio']}")
                                encontrado = True
                            
                        if encontrado == False:
                            print("No se encontro ese juego")
    
                case "5":
                    if not inventario:
                        print("No hay juegos registrados.")
                    else:
                    
                        buscar_jue = input("Escribe el nombre del juego al que quieras agregar stcok: ")
                    
                        for juego in inventario:
                            if juego['juego'] == buscar_jue:
                                print("-------------------------")
                                print(f"   juego: {juego['juego']}")
                                print(f"   Precio: ${juego['precio']}")
                                print(f"   Stock: {juego['stock']}")
                                print(f"   Valoracion: {juego['valoracion']}★")
                                print("-------------------------")
                                nuevo_stock = int(input("Cuanto stock deséas agregar "))
                                if nuevo_stock <= 0:
                                    print("Datos inválidos. Intenta de nuevo.")
                                else:
                                    juego['stock'] = juego['stock'] + nuevo_stock
                                    print("Nuevo stock: ")
                                    print(f"   Stock: {juego['stock']}")
                                encontrado = True
                            
                        if encontrado == False:
                            print("No se encontro ese juego")
    
                case "6":
    
                    if not inventario:
                        print("No hay juegos registrados.")
                    else:
                    
                        buscar_jue = input("Escribe el nombre del juego al que quieras cambiar la valoración: ")
                    
                        for juego in inventario:
                            if juego['juego'] == buscar_jue:
                                print("-------------------------")
                                print(f"   juego: {juego['juego']}")
                                print(f"   Precio: ${juego['precio']}")
                                print(f"   Stock: {juego['stock']}")
                                print(f"   Valoracion: {juego['valoracion']}★")
                                print("-------------------------")
                                nueva_valoracion = int(input("Cual el la nueva valoracion "))
                                if nueva_valoracion < 1 or nueva_valoracion > 5 :
                                    print("Datos inválidos. Intenta de nuevo.")
                                else:
                                    juego['valoracion'] = nueva_valoracion
                                    print("Nueva valoracion: ")
                                    print(f"   Valoracion: {juego['valoracion']}★")
                                encontrado = True
                            
                        if encontrado == False:
                            print("No se encontro ese juego")
                            
                case "7":
                    if not inventario:
                        print("No hay juegos registrados.")
                    else:
                        buscar_jue = input("Escribe el nombre del juego al que quieras borrar del inventario: ")
                    
                        for juego in inventario:
                            if juego['juego'] == buscar_jue:
                                inventario.remove(juego)
                                encontrado = True
                            
                        if encontrado == False:
                            print("No se encontro ese juego")
        
                case "8":
                    print("Saliendo del programa...")
                    usuario = 0
                    break
    
                case _:
    
                    print("Opción no válida. Intenta otra vez.")
                    
    elif usuario == 2:
        print("BIENVENIDO A EMILITUS'S STORE: Juegos y Mas!")
        print(" ")
        print("1. Ver juegos en stock")
        print("2. Buscar juego para comprar")
        print("3. Sugerir cambio de valoracion")
        print("4. Salir")
        print(" ")
        
        encontrado = False
    
    
        opcion2 = input("Elige una opción: ")
        print(" ")
        
        match opcion2:
            case "1":
                if not inventario:
                    print("No hay juegos registrados aún.")
                else:
                    print("\njuegos registrados:")
                    print("-------------------------")
                    for i, juego in enumerate(inventario, 1):
                        print(f"{i}. juego: {juego['juego']}")
                        print(f"   Precio: ${juego['precio']}")
                        print(f"   Stock: {juego['stock']}")
                        print(f"   Valoracion: {juego['valoracion']}★")
                        print("-------------------------")
                            
            case "2":
                if not inventario:
                    print("No hay juegos registrados.")
                else:
                    buscar_jue = input("Escribe el nombre del juego que quieras buscar: ")
                        
                    for juego in inventario:
                        if juego['juego'] == buscar_jue:
                            print("-------------------------")
                            print(f"   juego: {juego['juego']}")
                            print(f"   Precio: ${juego['precio']}")
                            print(f"   Stock: {juego['stock']}")
                            print(f"   Valoracion: {juego['valoracion']}★")
                            print("-------------------------")
                            encontrado = True
                                
                            print(" ")
                            print(f"¿Quieres comprar el {juego['juego']}")
                            print("1. Si")
                            print("2. No")
                            print(" ")
                            comprar = int(input("Decide: "))
                            print(" ")
                                
                            if comprar == 1:
                                nueva_compra = int(input("¿Cuantas unidades quieres comprar?: "))
                                if nueva_compra <= 0:
                                    print("Datos inválidos. Intenta de nuevo.")
                                else:
                                    if nueva_compra > juego['stock']:
                                        print("no hay suficiente stock para realizar esa compra.")
                                    else:
                                        juego['stock'] = juego['stock'] - nueva_compra
                                        aviso = True
                                        
                                        juegoVendido = juego['juego']
                                        UnidadesVendidas = nueva_compra
                                        
                                        nueva_venta = {
                                            "juegoVendido": juegoVendido,
                                            "UnidadesVendidas": UnidadesVendidas,
                                        }
                                        ventas.append(nueva_venta)
                                        
                            else:
                                print(" ")
                        
                            if encontrado == False:
                                print("No se encontro ese juego")
                                
            case "3":
                if not inventario:
                    print("No hay juegos registrados.")
                else:
                    
                    buscar_jue = input("Escribe el nombre del juego del que quieras enviar una reseña: ")
                    
                    for juego in inventario:
                        if juego['juego'] == buscar_jue:
                            print("-------------------------")
                            print(f"   juego: {juego['juego']}")
                            print(f"   Precio: ${juego['precio']}")
                            print(f"   Stock: {juego['stock']}")
                            print(f"   Valoracion: {juego['valoracion']}★")
                            print("-------------------------")
                            nueva_resenia = int(input("deja una reeseña del 1 al 5: "))
                            if nueva_resenia < 1 or nueva_resenia > 5 :
                                print("Datos inválidos. Intenta de nuevo.")
                            else:
                                juegoResenia = juego['juego']
                                recomendacionN = nueva_resenia
                                
                                nueva_recomendacion = {
                                    "juegoReseniado": juegoResenia,
                                    "Recomendacion": recomendacionN,
                                }
                                resenias.append(nueva_recomendacion)
                                
                                print("Reseña enviada...")
                                avisoResenia = True
                            encontrado = True
                            
                        if encontrado == False:
                            print("No se encontro ese juego")
                            
            case "4":
                print("Saliendo del programa...")
                usuario = 0
    
            case _:
    
                print("Opción no válida. Intenta otra vez.")
                    