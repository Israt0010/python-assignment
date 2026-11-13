# Simple Shopping Cart

# Taking customer's name
name = input("Enter Customer Name:")

print()

# Taking product names and prices
product1 = input("Enter Product 1 Name:")
price1 = float(input("Enter Product 1 Price:"))

print()

product2 = input("Enter Product 2 Name:")
price2 = float(input("Enter Product 2 Price:"))

print()

product3 = input("Enter Product 3 Name:")
price3 = float(input("Enter Product 3 Price:"))

print()

# Calculating subtotal
subtotal = price1 + price2 + price3

print()
# Determining discount rate
if subtotal >= 5000:
    discount_rate = 0.20
elif subtotal >= 3000:
    discount_rate = 0.10
elif subtotal >= 1000:
    discount_rate = 0.05
else:
    discount_rate = 0

print()
# Calculating discount
discount = subtotal*discount_rate

print()
# Calculating final total
final_total = subtotal - discount

print()

# Displaying shopping summary using f-string
print(f"Customer Name: {name}")

print()
print(f"Product 1: {product1}")
print(f"Price: {price1}")

print()
print(f"Product 2: {product2}")
print(f"Price: {price2}")

print()
print(f"Product 3: {product3}")
print(f"Price: {price3}")

print()
print(f"Subtotal: {subtotal}")
print(f"Discount: {discount}")
print(f"Final Total: {final_total}")
