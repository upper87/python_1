name = "Иван"
age = 32
job_title = "Бухгалтер"

message1 = "Уважаемый, " + name + " " + job_title + " " + "поздравляем Вас с днем рождения " + str(age) + " - хороший возраст"
message2 = "Уважаемый, %s %s поздравляем Вас с днем рождения %s - хороший возраст" % (name, job_title, age)
message3 = "Уважаемый, {1} {2} поздравляем Вас с днем рождения {0} - хороший возраст".format(name, job_title, age)
message4 = f"Уважаемый, {name.upper()} {job_title} поздравляем Вас с днем рождения {age+1} - хороший возраст"
print(message1)
print(message2)
print(message3)
print(message4)
