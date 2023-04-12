string = input("Введите произвольный текст: ")
check_id = string[:3]
check_dig = string[3:].isdigit()
if check_id == "id:" and check_dig == True:
    print("Да")
else:
    print("Нет")