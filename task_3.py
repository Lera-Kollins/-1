list_players = ["Маша", "Петя", "Саша", "Оля", "Кирилл", "Коля"]

# TODO Разделите участников на две команды
a = len(list_players) // 2   # кол-во игроков в одной команде
list_1 = list_players[:a]
list_2 = list_players[a:]

print(list_1)
print(list_2)
