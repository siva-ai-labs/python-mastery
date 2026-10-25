
# SIVA AI LABS
# Python Data Structures: Dictionary
# Real-world use case: Product Catalog Management

products = {
    "ART1001": {
        "name": "Cotton T-Shirt",
        "category": "Men",
        "price": 199,
        "stock": 50
    },
    "ART1002": {
        "name": "Summer Dress",
        "category": "Women",
        "price": 399,
        "stock": 25
    },
    "ART1003": {
        "name": "Blue Jeans",
        "category": "Men",
        "price": 599,
        "stock": 8
    }
}


# 1. Add a new product
def add_product(article_code, name, category, price, stock):
    if article_code in products:
        return "Product already exists"

    if price <= 0 or stock < 0:
        return "Invalid price or stock"

    products[article_code] = {
        "name": name,
        "category": category,
        "price": price,
        "stock": stock
    }

    return "Product added successfully"


# 2. Get product by article code
def get_product(article_code):
    return products.get(article_code, "Product not found")


# 3. Update product price
def update_price(article_code, new_price):
    if article_code not in products:
        return "Product not found"

    if new_price <= 0:
        return "Price must be positive"

    products[article_code]["price"] = new_price
    return "Price updated successfully"


# 4. Update stock
def update_stock(article_code, quantity):
    if article_code not in products:
        return "Product not found"

    if quantity < 0:
        return "Stock cannot be negative"

    products[article_code]["stock"] = quantity
    return "Stock updated successfully"


# 5. Delete a product
def delete_product(article_code):
    if article_code not in products:
        return "Product not found"

    del products[article_code]
    return "Product deleted successfully"


# 6. Search products by category
def search_by_category(category):
    return {
        code: product
        for code, product in products.items()
        if product["category"].lower() == category.lower()
    }


# 7. Find products with low stock
def get_low_stock_products(threshold=10):
    return {
        code: product
        for code, product in products.items()
        if product["stock"] < threshold
    }


# 8. Calculate total inventory value
def calculate_inventory_value():
    return sum(
        product["price"] * product["stock"]
        for product in products.values()
    )


# Test all operations
print("1. Add product:")
print(add_product("ART1004", "Winter Jacket", "Men", 999, 15))

print("\n2. Get product:")
print(get_product("ART1001"))

print("\n3. Update price:")
print(update_price("ART1001", 249))

print("\n4. Update stock:")
print(update_stock("ART1003", 5))

print("\n5. Products in Men category:")
print(search_by_category("Men"))

print("\n6. Low stock products:")
print(get_low_stock_products())

print("\n7. Total inventory value:")
print(calculate_inventory_value())

print("\n8. Delete product:")
print(delete_product("ART1002"))
