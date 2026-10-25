
# Real-world use case: Retail Customer Analytics
# Data structures: Dictionary + Set

store_customers = {
    "SE001": {"C101", "C102", "C103"},
    "SE002": {"C102", "C104", "C105"},
    "SE003": {"C101", "C105", "C106"}
}


# 1. Register a customer at a store
def register_customer(store_id, customer_id):
    if store_id not in store_customers:
        store_customers[store_id] = set()

    store_customers[store_id].add(customer_id)


# 2. Get unique customer count per store
def get_customer_count(store_id):
    return len(store_customers.get(store_id, set()))


# 3. Find customers common to two stores
def get_common_customers(store1, store2):
    customers1 = store_customers.get(store1, set())
    customers2 = store_customers.get(store2, set())

    return customers1 & customers2


# 4. Find customers exclusive to one store
def get_exclusive_customers(store1, store2):
    customers1 = store_customers.get(store1, set())
    customers2 = store_customers.get(store2, set())

    return customers1 - customers2


# 5. Find all unique customers
def get_all_unique_customers():
    all_customers = set()

    for customers in store_customers.values():
        all_customers.update(customers)

    return all_customers


# 6. Find customers visiting multiple stores
def get_multi_store_customers():
    customer_counts = {}

    for customers in store_customers.values():
        for customer_id in customers:
            customer_counts[customer_id] = (
                customer_counts.get(customer_id, 0) + 1
            )

    return {
        customer_id
        for customer_id, count in customer_counts.items()
        if count > 1
    }


# Test the application
register_customer("SE001", "C107")
register_customer("SE001", "C101")  # Duplicate ignored

print("SE001 customer count:", get_customer_count("SE001"))

print(
    "Common customers:",
    sorted(get_common_customers("SE001", "SE002"))
)

print(
    "Exclusive customers:",
    sorted(get_exclusive_customers("SE001", "SE002"))
)

print(
    "All unique customers:",
    sorted(get_all_unique_customers())
)

print(
    "Multi-store customers:",
    sorted(get_multi_store_customers())
)
