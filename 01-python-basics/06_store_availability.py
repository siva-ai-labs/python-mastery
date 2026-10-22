
# 06_store_availability.py

stores = {
    "SE001": {
        "name": "Stockholm Central",
        "articles": {
            "ART1001": 15,
            "ART1002": 0
        }
    },
    "SE002": {
        "name": "Mall of Scandinavia",
        "articles": {
            "ART1001": 8,
            "ART1002": 12
        }
    }
}


def check_availability(store_id, article_id):
    store = stores.get(store_id)

    if store is None:
        return "Store not found"

    stock = store["articles"].get(article_id)

    if stock is None:
        return "Article not found"

    if stock > 0:
        return f"Available: {stock} units"

    return "Out of stock"


print(check_availability("SE001", "ART1001"))
print(check_availability("SE001", "ART1002"))
print(check_availability("SE002", "ART1002"))
