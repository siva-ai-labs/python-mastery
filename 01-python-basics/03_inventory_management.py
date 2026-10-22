
# 03_inventory_management.py

inventory = {
    "T-Shirt": 120,
    "Jeans": 8,
    "Jacket": 0,
    "Shoes": 25,
    "Hoodie": 4
}

LOW_STOCK_THRESHOLD = 10

print("--- Inventory Report ---")

for product, quantity in inventory.items():

    if quantity == 0:
        status = "OUT OF STOCK"
    elif quantity < LOW_STOCK_THRESHOLD:
        status = "LOW STOCK"
    else:
        status = "AVAILABLE"

    print(f"{product}: {quantity} units - {status}")
