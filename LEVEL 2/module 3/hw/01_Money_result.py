import urllib.request, json
class Money:
    def __init__(self, rubles:int, kopecks: int):
        self.rubles = rubles
        self.kopecks = kopecks
    def __add__(self, other_money):
        res_r = self.rubles + other_money.rubles
        res_k = self.kopecks + other_money.kopecks
        if res_k >= 100:
            res_r += 1
            res_k -= 100
        # if res_k < 10 and res_k % 10 != 0 :
        #     res_k /= 10
        return f"при сложении получилось {res_r} руб {res_k} к"
    def __sub__(self, other_money):
        res_r = self.rubles - other_money.rubles
        res_k = self.kopecks - other_money.kopecks
        if res_k < 0:
            res_r -= 1
            res_k = 100 - abs(res_k)
        return f"после вычитания осталось {res_r} руб {res_k} к"
    def __mul__(self, other_money):
        res_r = self.rubles * other_money.rubles
        res_k = self.kopecks/10 * other_money.kopecks/10
        return f"при умножении получилось {res_r} руб {int(res_k)} к"

    def __gt__(self, other_money):
        if self.rubles > other_money.rubles:
            return f"{self.rubles} {self.kopecks} > {other_money.rubles} {other_money.kopecks}"
        elif self.rubles == other_money.rubles:
            if self.kopecks > other_money.kopecks:
                return f"{self.rubles} {self.kopecks} > {other_money.rubles} {other_money.kopecks}"
            else:
                return f"не больше!"
        else:
            return f"не больше!"
    def __eq__(self, other_money):
        if self.rubles == other_money.rubles and self.kopecks == other_money.kopecks:
            return f" деньги равны"
        else:
            return f"деньги не равны"
    #
    def __lt__(self, other_money):
        if self.rubles < other_money.rubles:
            return f"{self.rubles} {self.kopecks} < {other_money.rubles} {other_money.kopecks}"
        elif self.rubles == other_money.rubles:
            if self.kopecks < other_money.kopecks:
                return f"{self.rubles} {self.kopecks} < {other_money.rubles} {other_money.kopecks}"
            else:
                return f"не меньше!"
        else:
            return f"не меньше!"
    def convert(self):
        pass


money_sum1 = Money(10, 40)
money_sum2 = Money(20, 45)
money_result_sum = money_sum1 + money_sum2
print(money_result_sum)  # 31руб 5коп
money_result = money_sum1 - money_sum2
print(money_result)
money_result = money_sum1 * money_sum2
print(money_result)
money_result = money_sum1 > money_sum2
print(money_sum1 > money_sum2)

print(money_sum1 == money_sum2)
print(money_sum1 < money_sum2)
percent = money_sum1.rubles * 100 / (money_sum1.rubles + money_sum2.rubles)
print(f"проценты {int(percent)} %")
percent_sum = money_sum1.rubles / int(percent) * 100
print(int(percent_sum))
# data_dict = {}
# data = urllib.request.urlopen("https://www.cbr-xml-daily.ru/daily_json.js").read()
# data_dict = json.loads(data)
# usd = data_dict["USD"]
# print(usd)

print(money_sum1.rubles, money_sum1.kopecks)
print(money_sum2.rubles, money_sum2.kopecks)