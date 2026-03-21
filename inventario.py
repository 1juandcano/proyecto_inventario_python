# Sistema de Inventario

inventario = []  # Lista de productos


def agregar_producto():
    # Pedir nombre
    nombre = input("Ingrese el nombre del producto: ")

    # Validar precio
    while True:
        try:
            precio = float(input("Ingrese el precio: "))
            if precio < 0:
                print("No puede ser negativo.")
            else:
                break
        except ValueError:
            print("Ingrese un número válido.")

    # Validar cantidad
    while True:
        try:
            cantidad = int(input("Ingrese la cantidad: "))
            if cantidad < 0:
                print("No puede ser negativa.")
            else:
                break
        except ValueError:
            print("Ingrese un número entero.")

    # Crear y guardar producto
    producto = {
        "nombre": nombre,
        "precio": precio,
        "cantidad": cantidad
    }

    inventario.append(producto)
    print("Producto agregado.\n")


def mostrar_inventario():
    # Mostrar productos
    if not inventario:
        print("Inventario vacío.\n")
        return

    for producto in inventario:
        print(f"Producto: {producto['nombre']} | Precio: {producto['precio']} | Cantidad: {producto['cantidad']}")
    print()


def calcular_estadisticas():
    # Calcular totales
    if not inventario:
        print("No hay datos.\n")
        return

    valor_total = 0
    total_productos = 0

    for producto in inventario:
        valor_total += producto["precio"] * producto["cantidad"]
        total_productos += producto["cantidad"]

    print(f"Valor total: {valor_total}")
    print(f"Total productos: {total_productos}\n")


def main():
    # Menú principal
    while True:
        print("1. Agregar producto")
        print("2. Mostrar inventario")
        print("3. Calcular estadísticas")
        print("4. Salir")

        opcion = input("Seleccione: ")

        if opcion == "1":
            agregar_producto()
        elif opcion == "2":
            mostrar_inventario()
        elif opcion == "3":
            calcular_estadisticas()
        elif opcion == "4":
            print("Saliendo...")
            break
        else:
            print("Opción inválida.\n")


main()