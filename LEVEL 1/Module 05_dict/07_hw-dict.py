# Дано описание товара
item = {
    "name": "Кроссовки",
    "price": "7540.5",
    "currency": "rub",
    "color": "white"
    }
# Ключи точно известны, а вот значения могут быть разные(эти значения даны для примера)

# Также известен курс доллара:
dollar_rate = 74.12
cost = float(input("Стоимость кроссовок: "))
item["price"] = cost
# Вычислите цену товара в долларах
price_usd = float(item["price"]) / dollar_rate
print(price_usd)