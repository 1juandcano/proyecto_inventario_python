# ---------------------------------------------
# Simple Inventory Program
# ---------------------------------------------
# This program registers a product by asking the user
# for the product name, price, and quantity.
# It validates the numeric inputs and calculates
# the total cost of the product in the inventory.
# ---------------------------------------------

# Ask the user for the product name
product_name = input("Enter the product name: ")

# ---------------------------------------------
# Validate the price input
# The program keeps asking until a valid number is entered
# ---------------------------------------------
while True:
    price_input = input("Enter the unit price: ")

    try:
        price = float(price_input)

        if price < 0:
            print("Invalid value. Price cannot be negative.")
        else:
            break

    except ValueError:
        print("Invalid input. Please enter a valid number.")


# ---------------------------------------------
# Validate the quantity input
# The program keeps asking until a valid integer is entered
# ---------------------------------------------
while True:
    quantity_input = input("Enter the quantity: ")

    try:
        quantity = int(quantity_input)

        if quantity < 0:
            print("Invalid value. Quantity cannot be negative.")
        else:
            break

    except ValueError:
        print("Invalid input. Please enter a whole number.")


# ---------------------------------------------
# Calculate the total cost
# ---------------------------------------------
total_cost = price * quantity


# ---------------------------------------------
# Display the results in the console
# ---------------------------------------------
print("\n----- PRODUCT SUMMARY -----")
print(f"Product: {product_name}")
print(f"Unit Price: {price}")
print(f"Quantity: {quantity}")
print(f"Total Cost: {total_cost}")


# ----------------------------------------------------------
# Program description:
# This program simulates a very simple inventory system.
# It asks the user for the product name, unit price, and
# quantity available. The program validates that price and
# quantity are numeric values and not negative. After the
# validation, it calculates the total cost by multiplying
# price and quantity, and then prints a summary in the console.
# ----------------------------------------------------------