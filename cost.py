cost = int(input("Стоимость покупки "))
if cost > 1000:
	cost = cost - (cost * 0.15)
print("К оплате:", cost)