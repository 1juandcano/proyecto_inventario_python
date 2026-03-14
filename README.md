# Programa de Inventario Simple en Python

# Descripción del Proyecto

Este proyecto es un **programa básico de inventario desarrollado en Python**.

El objetivo del programa es permitir que un usuario registre información básica de un producto y calcular automáticamente el **costo total del inventario** para ese producto.

Este programa está diseñado especialmente para **personas que están aprendiendo programación desde cero**.

El sistema solicita al usuario tres datos:

- Nombre del producto
- Precio unitario del producto
- Cantidad disponible del producto

Después de ingresar estos datos, el programa:

1. Verifica que el precio ingresado sea un número válido.
2. Verifica que la cantidad sea un número entero válido.
3. Evita valores negativos.
4. Calcula el costo total del producto.
5. Muestra un resumen del producto en la consola.

---

#  Objetivos del Proyecto

Este programa sirve para aprender y practicar conceptos fundamentales de programación como:

- Entrada de datos por teclado
- Uso de variables
- Validación de datos
- Manejo de errores
- Uso de ciclos (`while`)
- Uso de condiciones (`if`)
- Operaciones matemáticas
- Mostrar información en consola

---

#  Requisitos

Para ejecutar este programa necesitas instalar:

- **Python 3**
- **Git (para clonar el repositorio)**

---

# Verificar si Python está instalado

Abre una terminal y escribe:

```bash
python3 --version
```

Si Python está instalado verás algo como:

```
Python 3.10.6
```

Si no tienes Python instalado puedes descargarlo desde:

https://www.python.org/downloads/

---

#  Cómo Clonar el Repositorio

Si el proyecto está en GitHub, puedes descargarlo usando **Git**.

## Paso 1: Verificar que Git esté instalado

En la terminal escribe:

```bash
git --version
```

Si Git está instalado verás algo como:

```
git version 2.34.1
```

Si no tienes Git puedes instalarlo desde:

https://git-scm.com/downloads

---

## Paso 2: Copiar la URL del repositorio

En la página de GitHub del proyecto, presiona el botón **Code** y copia la URL del repositorio.

Ejemplo:

```
https://github.com/usuario/inventario-python.git
```

---

## Paso 3: Clonar el repositorio

En la terminal ejecuta:

```bash
git clone https://github.com/usuario/inventario-python.git
```

Esto descargará todos los archivos del proyecto a tu computadora.

---

## Paso 4: Entrar en la carpeta del proyecto

Después de clonar el repositorio, entra a la carpeta:

```bash
cd inventario-python
```

---

# Estructura del Proyecto

El proyecto tiene una estructura simple:

```
inventario-python/
│
├── inventory.py
└── README.md
```

Archivos del proyecto:

**inventory.py**  
Contiene el código del programa.

**README.md**  
Contiene la documentación del proyecto.

---

# ▶Cómo Ejecutar el Programa

Una vez dentro de la carpeta del proyecto, ejecuta el programa con:

```bash
python3 inventory.py
```

---

#  Ejemplo de Ejecución del Programa

Cuando ejecutes el programa verás algo como esto:

```
Enter the product name: Laptop
Enter the unit price: 800
Enter the quantity: 3

----- PRODUCT SUMMARY -----
Product: Laptop
Unit Price: 800
Quantity: 3
Total Cost: 2400
```

Explicación:

El programa realiza el cálculo:

```
800 × 3 = 2400
```

Ese es el costo total del producto en el inventario.

---


---

# xplicación del Código Paso a Paso

---

#  Solicitar el nombre del producto

```python
product_name = input("Enter the product name: ")
```

La función `input()` permite que el usuario escriba información en la consola.

Ejemplo:

```
Enter the product name: Apple
```

El valor ingresado se guarda en la variable:

```
product_name
```

Una **variable** es un espacio donde el programa guarda información.

---

#  Validar el precio del producto

El programa debe asegurarse de que el precio sea un número válido.

Para esto se usa un ciclo:

```python
while True:
```

Esto significa que el programa seguirá preguntando hasta recibir un valor correcto.

Solicitar precio:

```python
price_input = input("Enter the unit price: ")
```

Convertir el valor a número:

```python
price = float(price_input)
```

Ejemplo:

```
"15.50" → 15.50
```

Si el valor es negativo:

```python
if price < 0:
```

El programa mostrará un error.

---

# Manejo de errores

```python
except ValueError:
```

Si el usuario escribe algo que no es un número, el programa mostrará un mensaje de error en lugar de fallar.

---

#  Validar la cantidad

Se usa la función:

```python
quantity = int(quantity_input)
```

`int()` convierte el valor ingresado en un número entero.

Ejemplos válidos:

```
1
5
10
100
```

---

#  Calcular el costo total

El cálculo se hace multiplicando:

```
precio × cantidad
```

Código:

```python
total_cost = price * quantity
```

---

#  Mostrar el resultado

El programa imprime un resumen del producto:

```python
print("\n----- PRODUCT SUMMARY -----")
print(f"Product: {product_name}")
print(f"Unit Price: {price}")
print(f"Quantity: {quantity}")
print(f"Total Cost: {total_cost}")
```

---

# Conceptos de Programación Utilizados

## Variables

Guardan datos.

```
product_name
price
quantity
total_cost
```

## Entrada de Datos

Permite que el usuario escriba información.

```
input()
```

## Ciclos

Repiten instrucciones.

```
while
```

## Condicionales

Permiten tomar decisiones.

```
if
```

## Manejo de errores

Evita que el programa se rompa.

```
try
except
```

---

Gracias por leer el documento.