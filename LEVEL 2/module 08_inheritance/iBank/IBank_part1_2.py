class Account:
    def __init__(self, name: str, passport: str, phone_number: str, start_balance: int = 0):
        self.name = name
        self.passport = passport
        self.phone_number = phone_number
        # self.balance = start_balance
        self.__balance = start_balance  # TODO: Закрываем прямой доступ к балансу

    def full_info(self) -> str:
        """
        Полная информация о счете в формате: "Иван баланс: 100 руб. паспорт: 3200 123456 т.+7-900-200-02-03"
        """
        return f"{self.name} баланс: {self.balance} руб. паспорт: {self.passport} т.{self.phone_number}"

    def __repr__(self) -> str:
        """
        :return: Информацию о счете в виде строки в формате "Иван баланс: 100 руб."
        """
        return f"{self.name} баланс: {self.balance} руб."

    # TODO: реализуйте getter для просмотра баланса
    #  Подробнее тут: https://pythobyte.com/using-getters-and-setters-in-python-5205-840ed13f/
    @property
    def balance(self) -> int:
        return self.__balance

    def deposit(self, amount: int) -> None:
        """
        Внесение суммы на текущий счет
        :param amount: сумма
        """
        if type(amount) == int:
            if amount > 0:
                self.__balance += amount
            else:
                raise ValueError(f"Только целое число больше нуля")
        else:
            raise ValueError(f"Только целое число больше нуля")

    def withdraw(self, amount: int) -> None:
        if type(amount) == int:
            if amount > 0:
                if self.__balance - amount < 0:
                    raise ValueError(f"Сумма вычета выше депозита")
                else:
                    self.__balance -= amount
            else:
                raise ValueError(f"Только целое число больше нуля")
        else:
            raise ValueError(f"Только целое число больше нуля")


# Создаем тестовый аккаунт:
account1 = Account("Алексей", "3232 456124", "+7-901-744-22-99", start_balance=500)

# Вносим сумму на счет:
account1.deposit(600)
print(account1)

# Снимаем деньги со счета:
try:
    account1.withdraw(1100)
except ValueError as e:
    print(e)
print(account1)





# Пробуем снять еще:
# try:
#     account1.withdraw(1000)
# except ValueError as e:
#     print(e)
# print(account1)
