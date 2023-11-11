# TODO Напишите функцию find_common_participants

def find_common_participants(a, b, c = ','):
    razdel1 = set(a.split(c))
    razdel2 = set(b.split(c))
    summa = razdel1.intersection(razdel2)
    return sorted(summa)
participants_first_group = "Иванов|Петров|Сидоров"
participants_second_group = "Петров|Сидоров|Смирнов"
print(list(find_common_participants(participants_first_group, participants_second_group,)))

# TODO Провеьте работу функции с разделителем отличным от запятой
