
from collections import Counter, defaultdict
from decimal import Decimal

# Sample retail sales transactions
sales = [
    {
        "order_id": "ORD101",
        "store": "SE001",
        "customer": "C101",
        "article": "ART1001",
        "category": "Men",
        "quantity": 2,
        "unit_price": "199.00"
    },
    {
        "order_id": "ORD102",
        "store": "SE002",
        "customer": "C102",
        "article": "ART1002",
        "category": "Women",
        "quantity": 1,
        "unit_price": "399.00"
    },
    {
        "order_id": "ORD103",
        "store": "SE001",
        "customer": "C101",
        "article": "ART1003",
        "category": "Men",
        "quantity": 1,
        "unit_price": "599.00"
    },
    {
        "order_id": "ORD104",
        "store": "SE003",
        "customer": "C103",
        "article": "ART1001",
        "category": "Men",
        "quantity": 3,
        "unit_price": "199.00"
    },
    {
        "order_id": "ORD105",
        "store": "SE002",
        "customer": "C102",
        "article": "ART1001",
        "category": "Men",
        "quantity": 1,
        "unit_price": "199.00"
    }
]


def analyze_sales(transactions):
    # Count units sold per article
    article_sales = Counter()

    # Count orders placed by each customer
    customer_orders = Counter()

    # Group revenue by store
    store_revenue = defaultdict(lambda: Decimal("0.00"))

    # Group quantities by category
    category_sales = defaultdict(int)

    for sale in transactions:
        article = sale["article"]
        customer = sale["customer"]
        store = sale["store"]
        category = sale["category"]
        quantity = sale["quantity"]

        revenue = (
            Decimal(sale["unit_price"]) * quantity
        )

        article_sales[article] += quantity
        customer_orders[customer] += 1
        store_revenue[store] += revenue
        category_sales[category] += quantity

    print("\n1. Units sold per article")
    for article, quantity in article_sales.items():
        print(article, quantity)

    print("\n2. Top 2 best-selling articles")
    for article, quantity in article_sales.most_common(2):
        print(article, quantity)

    print("\n3. Revenue by store")
    for store, revenue in store_revenue.items():
        print(store, f"{revenue:.2f} SEK")

    print("\n4. Orders per customer")
    for customer, count in customer_orders.items():
        print(customer, count)

    print("\n5. Units sold by category")
    for category, quantity in category_sales.items():
        print(category, quantity)

    total_revenue = sum(
        store_revenue.values(),
        Decimal("0.00")
    )

    print("\n6. Total revenue")
    print(f"{total_revenue:.2f} SEK")


analyze_sales(sales)
