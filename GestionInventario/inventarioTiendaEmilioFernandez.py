inventario = []

while True:
    print("\n--- SISTEMA DE GESTIÓN DE INVENTARIO ---")
    print("1. Registrar nuevo producto")
    print("2. Mostrar todos los productos")
    print("3. Buscar producto por nombre")
    print("4. Reponer stock")
    print("5. Registrar nueva compra")
    print("6. Salir")

    opcion = input("Elige una opción: ")

    match opcion:
        case "1":
            nombrePro = input("Nombre del producto: ")
            try:
                precio = float(input("Precio: "))
                stock =  int(input("Stock: "))
            except ValueError:
                print("Precio o stock inválidas. Intenta de nuevo.")
                continue

            if precio <= 0 or stock < 0:
                print("Datos inválidos. Intenta de nuevo.")
            else:
                nuevo_producto = {
                    "producto": nombrePro,
                    "precio": precio,
                    "stock": stock
                }
                inventario.append(nuevo_producto)
                print(f"Producto {nombrePro} registrado con éxito.")

        case "2":
            if not inventario:
                print("No hay productos registrados aún.")
            else:
                print("\nProductos registrados:")
                print("-------------------------")
                for i, producto in enumerate(inventario, 1):
                    print(f"{i}. Producto: {producto['producto']}")
                    print(f"   Precio: ${producto['precio']}")
                    print(f"   Stock: {producto['stock']}")
                    print("-------------------------")

        case "3":
            if not inventario:
                print("No hay productos registrados.")
            else:
                buscar_pro = input("Escribe el nombre del producto que quieras buscar: ")
                
                for producto in inventario:
                    if producto['producto'] == buscar_pro:
                        print("-------------------------")
                        print(f"   Producto: {producto['producto']}")
                        print(f"   Precio: ${producto['precio']}")
                        print(f"   Stock: {producto['stock']}")
                        print("-------------------------")

        case "4":
            if not inventario:
                print("No hay productos registrados.")
            else:
                

        case "6":
            print("Saliendo del programa...")
            break

        case _:
            print("Opción no válida. Intenta otra vez.")