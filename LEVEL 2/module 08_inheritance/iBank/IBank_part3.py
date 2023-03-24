from typing import List


# класс для хранения информации об операциях
class Operation:
    # Типы операций храним в свойствах класса
    DEPOSIT = 'Пополнение'
    WITHDRAW = 'Снятие'
    TRANSFER_OUT = 'Перевод'
    TRANSFER_IN = 'Поступление'

    # Напоминаю: обращение к этим переменным происходит через имя класса, пример: Operation.WITHDRAW

    def __init__(self, type, amount, target_account=None):
        self.type = type
        self.amount = amount
        self.target_account = target_account

    def __repr__(self) -> str:
        """
        :return: возвращает строковое представление операции. Формат указан в 02_IBank_part2.md
        """
        str_out = f"{self.type} {self.amount} руб."
        if self.type == Operation.WITHDRAW:
            str_out += f"(комиссия:{int(Account.FEE/100 * self.amount)})"
        if self.type == Operation.TRANSFER_OUT:
            str_out += f" на счет клиента: {self.target_account.name}"
        if self.type == Operation.TRANSFER_IN:
            str_out += f" со счета клиента: {self.target_account.name}"
        return str_out


class Account:
    FEE = 2

    def __init__(self, name: str, passport: str, phone_number: str, start_balance: int = 0):
        self.name = name
        self.passport = passport
        self.phone_number = phone_number
        self.__balance = start_balance
        # историю храним как список объектов класса Operation, добавив свойство в конструктор:
        self.__history: List[Operation] = []

    @property
    def balance(self) -> int:
        return self.__balance

    def deposit(self, amount: int, to_history: bool = True) -> None:
        """
        Внесение суммы на текущий счет
        :param amount: сумма
        :param to_history: True - записывать операцию в историю, False - не записывать
        """
        self.__balance += amount
        if to_history:
            operation = Operation(amount, Operation.DEPOSIT)
            self.__history.append(operation)

    @staticmethod
    def calculate_fee(amount: int) -> int:
        return int(amount * (100 + Account.FEE) / 100)

    def withdraw(self, amount: int, to_history: bool = True) -> None:
        """
        Снятие суммы с текущего счета
        :param amount: сумма
        """
        amount_with_fee = Account.calculate_fee(amount)
        if self.__balance - amount_with_fee >= 0:
            self.__balance -= amount_with_fee
            if to_history:
                operation = Operation(Operation.WITHDRAW, amount)
                self.__history.append(operation)
        else:
            raise ValueError("Недостаточно денег на счете")

    def transfer(self, target_account: 'Account', amount: int) -> None:
        """
        Перевод денег на счет другого клиента
        :param target_account: счет клиента для перевода
        :param amount: сумма перевода
        :return:
        """
        self.withdraw(amount, to_history=False)
        transfer_in = Operation(Operation.TRANSFER_IN, amount, self)
        transfer_out = Operation(Operation.TRANSFER_OUT, amount, target_account)
        self.__history.append(transfer_out)
        target_account.__history.append(transfer_in)
        target_account.deposit(amount, to_history=False)

    def get_history(self) -> List[Operation]:
        """
        :return: возвращаем историю операций в виде списка операций
        """
        return self.__history


account1 = Account("Иван", "3230 634563", "+7-900-765-12-34", 1000)
account2 = Account("Петр", "3230 634563", "+7-900-765-12-34", 200)

try:
    account1.withdraw(300)
except ValueError as e:
    print(e)

try:
    account1.withdraw(500)
except ValueError as e:
    print(e)

for operation in account1.get_history():
    print(operation)