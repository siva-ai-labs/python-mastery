
# SIVA AI LABS
# Python Data Structures - Nested Dictionary
# Use case: Multi-Store Inventory Management

inventory = {
    "SE001": {
        "ART1001": 50,
        "ART1002": 20,
        "ART1003": 0
    },
    "SE002": {
        "ART1001": 15,
        "ART1002": 0,
        "ART1003": 8
    },
    "SE003": {
        "ART1001": 0,
        "ART1002": 12,
        "ART1003": 5
    }
}


# 1. Get stock for an article at a store
def get_stock(store_id, article_code):
    return inventory.get(store_id, {}).get(article_code, 0)


# 2. Update stock
def update_stock(store_id, article_code, quantity):
    if store_id not in inventory:
        return "Store not found"

    if article_code not in inventory[store_id]:
        return "Article not found"

    if quantity < 0:
        return "Stock cannot be negative"

    inventory[store_id][article_code] = quantity
    return "Stock updated successfully"


# 3. Find stores with available stock
def find_available_stores(article_code):
    available_stores = {}

    for store_id, articles in inventory.items():
        stock = articles.get(article_code, 0)

        if stock > 0:
            available_stores[store_id] = stock

    return available_stores


# 4. Calculate total stock across stores
def get_total_stock(article_code):
    return sum(
        articles.get(article_code, 0)
        for articles in inventory.values()
    )


# 5. Find out-of-stock articles per store
def get_out_of_stock_articles(store_id):
    articles = inventory.get(store_id)

    if articles is None:
        return "Store not found"

    return [
        article_code
        for article_code, stock in articles.items()
        if stock == 0
    ]


# 6. Add a new article to a store
def add_article(store_id, article_code, stock):
    if store_id not in inventory:
        return "Store not found"

    if stock < 0:
        return "Stock cannot be negative"

    if article_code in inventory[store_id]:
        return "Article already exists"

    inventory[store_id][article_code] = stock
    return "Article added successfully"


# Test the operations
print("Stock:", get_stock("SE001", "ART1001"))

print("Available stores:", find_available_stores("ART1001"))

print("Total stock:", get_total_stock("ART1001"))

print("Out of stock:", get_out_of_stock_articles("SE001"))

print("Update:", update_stock("SE001", "ART1001", 40))

print("New stock:", get_stock("SE001", "ART1001"))

print("Add article:", add_article("SE003", "ART1004", 25))
