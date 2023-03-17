items = [
    {"name": "Кроссовки", "price": "7540.5", "currency": "rub"},
    {"name": "Шорты", "price": "1313.2", "currency": "rub"},
    {"name": "Кепка", "price": "738.0", "currency": "rub"},
    {"name": "Чемодан", "price": "2300.85", "currency": "rub"},
]
low_f = float(items[0]["price"])
for num, item in enumerate(items, 1):
    print(f"{num}. {item['name']}")
for low in items:
    if float(low["price"]) < low_f:
        low_f = float(low["price"])

print(low_f)
