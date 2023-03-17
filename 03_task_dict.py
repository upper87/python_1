keys = ['name', 'surname', 'age', 'rate']
values = ['Петр', 'Первый', 42, 1300]


person = dict(zip(keys, values))

print(person.get("age"))