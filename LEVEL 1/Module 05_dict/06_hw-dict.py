# С помощью словаря описаны два товара интернет магазина
product1 = {
    "id": 1,
    "title": "iPhone 9",
    "price": 124200,
    "brand": "Apple",
    "category": "smartphones"
}

product2 = {
    "id": 4,
    "title": "Redmi 10",
    "price": 18300,
    "brand": "Xiaomi",
    "category": "smartphones"
}
print(f"Товар {product1['title']} стоит {product1['price']} рублей, а {product2['title']} стоит {product2['price']} ")
# Выведите названия(title) товаров и их цены в формате: "Товар <такой-то> стоимостью <столько-то> рублей"
