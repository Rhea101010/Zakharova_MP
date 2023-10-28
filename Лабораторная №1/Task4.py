users = ['user1', 'user2', 'user3', 'user1', 'user4', 'user2']
Stata = {
    "Общее количество": 0,
    "Уникальные посещения": 0
}
new = len(users)
unique = set(users)
Stata["Общее количество"] = new
Stata["Уникальные посещения"] = len(unique)
print(Stata)
# TODO Добавьте словарь и замените в нем нулевые значения статисчикой посещений