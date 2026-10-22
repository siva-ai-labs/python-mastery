
# 02_shopping_cart.py

cart = [
    {"name": "T-Shirt", "price": 199, "quantity": 2},
    {"name": "Jeans", "price": 599, "quantity": 1},
    {"name": "Jacket", "price": 999, "quantity": 1}
]

total = 0

print("--- Shopping Cart ---")

for item in cart:
    subtotal = item["price"] * item["quantity"]
    total += subtotal

    print(
        f"{item['name']} x {item['quantity']} "
        f"= {subtotal} SEK"
    )

print("---------------------")
print(f"Total: {total} SEK")

if total >= 1500:
    print("Free delivery!")
else:
    print("Delivery charge: 49 SEK")
