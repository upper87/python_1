# Дан список сотрудников:
staff = [
    {
        'name': 'Григорий',
        'surname': 'Петров',
        'salary': 124300
    },
    {
        'name': 'Николай',
        'surname': 'Петров',
        'salary': 120000
    },
    {
        'name': 'Иван',
        'surname': 'Павлов',
        'salary': 34500
    },
    {
        'name': 'Василий',
        'surname': 'Кукушкин',
        'salary': 162500
    },
    {
        'name': 'Василий',
        'surname': 'Авдеев',
        'salary': 34500
    },
]

# print(staff['salary'])
staff.sort(key=lambda emp: (-emp["salary"], emp['surname']))
print("Список сотрудников отсортированный по уменьшению ЗП:")
for emp in staff:
    print(f"{emp['name']} {emp['surname']} {emp['salary']} ")


# 2. Найдите сумму зарплат трех самых низкооплачиваемых сотрудников:

# summa = 0
# for staf in staff[-3:]:
#     summa += staf['salary']
# print(summa)
print(sum(map(lambda emp: emp['salary'], staff[-3:])))
