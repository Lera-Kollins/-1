# TODO Напишите функцию find_common_participants
def find_common_participants(first_str, second_str, splitter=','):
    first_set = set(first_str.split(splitter))
    second_set = set(second_str.split(splitter))
    common_participants = first_set.intersection(second_set)
    list_common_participants = list(common_participants)
    list_common_participants.sort()
    return list_common_participants


participants_first_group = "Иванов|Петров|Сидоров"
participants_second_group = "Петров|Сидоров|Смирнов"

# TODO Провеьте работу функции с разделителем отличным от запятой
print(find_common_participants(participants_first_group, participants_second_group, splitter='|'))
