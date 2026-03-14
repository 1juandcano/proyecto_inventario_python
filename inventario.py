# ---------------------------------------------
<<<<<<< HEAD
# Programa de inventario
# ---------------------------------------------
# Este programa registra el producto que el usuario pida
# for the product name, price, and quantity.
# It validates the numeric inputs and calculates
# the total cost of the product in the inventory.
=======
# Programa simple de inventario
# ---------------------------------------------
# Este programa registra un producto preguntando al usuario
# por el nombre del producto, precio y cantidad.
# Valida las entradas numéricas y calcula
# el costo total del producto en el inventario.
>>>>>>> 0ee1643ee2b46f945b43343686e8f9317e98d9a7
# ---------------------------------------------

# Pedir al usuario el nombre del producto
nombre_producto = input("Ingrese el nombre del producto: ")

# ---------------------------------------------
# Validar la entrada del precio
# El programa seguirá preguntando hasta que se ingrese
# un número válido
# ---------------------------------------------
while True:
    entrada_precio = input("Ingrese el precio unitario: ")

    try:
        precio = float(entrada_precio)

        if precio < 0:
            print("Valor inválido. El precio no puede ser negativo.")
        else:
            break

    except ValueError:
        print("Entrada inválida. Por favor ingrese un número válido.")


# ---------------------------------------------
# Validar la entrada de la cantidad
# El programa seguirá preguntando hasta que se ingrese
# un número entero válido
# ---------------------------------------------
while True:
    entrada_cantidad = input("Ingrese la cantidad: ")

    try:
        cantidad = int(entrada_cantidad)

        if cantidad < 0:
            print("Valor inválido. La cantidad no puede ser negativa.")
        else:
            break

    except ValueError:
        print("Entrada inválida. Por favor ingrese un número entero.")


# ---------------------------------------------
# Calcular el costo total
# ---------------------------------------------
costo_total = precio * cantidad


# ---------------------------------------------
# Mostrar los resultados en la consola
# ---------------------------------------------
print("\n----- RESUMEN DEL PRODUCTO -----")
print(f"Producto: {nombre_producto}")
print(f"Precio unitario: {precio}")
print(f"Cantidad: {cantidad}")
print(f"Costo total: {costo_total}")


# ----------------------------------------------------------
# Descripción del programa:
# Este programa simula un sistema de inventario muy simple.
# Solicita al usuario el nombre del producto, el precio
# unitario y la cantidad disponible. El programa valida
# que el precio y la cantidad sean valores numéricos
# y que no sean negativos. Después de la validación,
# calcula el costo total multiplicando el precio por la
# cantidad y finalmente muestra un resumen en la consola.
# ----------------------------------------------------------
