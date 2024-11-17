
purchases = [
    {"item": "apple", "category": "fruit", "price": 1.2, "quantity": 10},
    {"item": "banana", "category": "fruit", "price": 0.5, "quantity": 5},
    {"item": "milk", "category": "dairy", "price": 1.5, "quantity": 2},
    {"item": "bread", "category": "bakery", "price": 2.0, "quantity": 3},
]

# 1. Общая выручка
def total_revenue(purchases):
    return sum(item['price'] * item['quantity'] for item in purchases)

# 2. Товары по категориям
def items_by_category(purchases):
    category_items = {}
    for item in purchases:
        category = item['category']
        if category not in category_items:
            category_items[category] = []
        if item['item'] not in category_items[category]:
            category_items[category].append(item['item'])
    return category_items

# 3. Покупки дороже заданной цены
def expensive_purchases(purchases, min_price=1.0):
    return [item for item in purchases if item['price'] >= min_price]

# 4. Средняя цена по категориям
def average_price_by_category(purchases):
    category_sums = {}
    category_counts = {}
    for item in purchases:
        category = item['category']
        price = item['price']
        if category not in category_sums:
            category_sums[category] = 0
            category_counts[category] = 0
        category_sums[category] += price
        category_counts[category] += 1
    return {category: round(category_sums[category] / category_counts[category], 2) for category in category_sums}

# 5. Категория с наибольшим количеством проданных товаров
def most_frequent_category(purchases):
    category_quantities = {}
    for item in purchases:
        category = item['category']
        quantity = item['quantity']
        if category not in category_quantities:
            category_quantities[category] = 0
        category_quantities[category] += quantity
    return max(category_quantities, key=category_quantities.get)

# Генерация отчёта
print(f"Общая выручка: {total_revenue(purchases)}")
print(f"Товары по категориям: {items_by_category(purchases)}")
print(f"Покупки дороже 1.0: {expensive_purchases(purchases, 1.0)}")
print(f"Средняя цена по категориям: {average_price_by_category(purchases)}")
print(f"Категория с наибольшим количеством проданных товаров: {most_frequent_category(purchases)}")


    