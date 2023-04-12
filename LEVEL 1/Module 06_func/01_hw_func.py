# Дан шестизначный номер билета. Определить, является ли билет счастливым.
# Решение реализовать в виде функции.
# Билет считается счастливым, если сумма его первых и последних цифр равны.

# def lucky_ticket(ticket_number):
#     strin = str(ticket_number)
#     a1 = strin[0]
#     a2 = strin[1]
#     a3 = strin[2]
#     a4 = strin[3]
#     a5 = strin[4]
#     a6 = strin[5]
#     if int(a1) + int(a2) + int(a3) == int(a4) + int(a5) + int(a6):
#         return ("Билет счастливый")
#     else:
#         return ("Билет не счастливый")
def lucky_ticket(ticket_number):
    if len(str(ticket_number)) < 6 or len(str(ticket_number)) > 6:
        return("В билете не 6 цифр, он не счастливый -(")
    else:
        a_1 = ticket_number // 100000
        a_2 = ticket_number % 100000 // 10000
        a_3 = ticket_number % 10000 // 1000
        a_4 = ticket_number % 1000 // 100
        a_5 = ticket_number % 100 // 10
        a_6 = ticket_number % 10
        if a_1 + a_2 + a_3 == a_4 + a_5 + a_6:
            return ("Билет счастливый")
        else:
            return("Билет не счастливый")

#
#     # TODO: your code here
#     pass
#
#
# # Тестируем функцию
print(lucky_ticket(123006))
print(lucky_ticket(12321))
print(lucky_ticket(436751))
print(lucky_ticket(436759))

# n = 121222
# if len(str(n)) < 6 or len(str(n)) > 6:
#     print("В билете меньше 6 цифр, он не счастливый -(")
# else:
#     a_1 = n // 100000
#     a_2 = n % 100000 // 10000
#     a_3 = n % 10000 // 1000
#     a_4 = n % 1000 // 100
#     a_5 = n % 100 // 10
#     a_6 = n % 10
#     if a_1 + a_2 + a_3 == a_4 + a_5 + a_6:
#         print("Билет счастливый")
#     else:
#         print("Билет не счастливый")
