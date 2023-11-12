# TODO  Напишите функцию count_letters
def count_letters(text):
    text = text.lower()
    default_count = 0
    dict_count_letters = {}
    for letter in text:
        if letter.isalpha():
            dict_count_letters[letter] = dict_count_letters.get(letter, default_count) + 1
    return dict_count_letters


# TODO Напишите функцию calculate_frequency
def calculate_frequency(dict_count_letters):
    dict_frequency_letters = {}
    total_number_of_letters = sum(dict_count_letters.values())
    for letter, count in dict_count_letters.items():
        dict_frequency_letters[letter] = count / total_number_of_letters
    return dict_frequency_letters


main_str = """
У лукоморья дуб зелёный;
Златая цепь на дубе том:
И днём и ночью кот учёный
Всё ходит по цепи кругом;
Идёт направо — песнь заводит,
Налево — сказку говорит.
Там чудеса: там леший бродит,
Русалка на ветвях сидит;
Там на неведомых дорожках
Следы невиданных зверей;
Избушка там на курьих ножках
Стоит без окон, без дверей;
Там лес и дол видений полны;
Там о заре прихлынут волны
На брег песчаный и пустой,
И тридцать витязей прекрасных
Чредой из вод выходят ясных,
И с ними дядька их морской;
Там королевич мимоходом
Пленяет грозного царя;
Там в облаках перед народом
Через леса, через моря
Колдун несёт богатыря;
В темнице там царевна тужит,
А бурый волк ей верно служит;
Там ступа с Бабою Ягой
Идёт, бредёт сама собой,
Там царь Кащей над златом чахнет;
Там русский дух… там Русью пахнет!
И там я был, и мёд я пил;
У моря видел дуб зелёный;
Под ним сидел, и кот учёный
Свои мне сказки говорил.
"""

# TODO Распечатайте в столбик букву и её частоту в тексте
dict_count_char = count_letters(main_str)
dict_frequency_char = calculate_frequency(dict_count_char)
for char, frequency in dict_frequency_char.items():
    print(f'{char}:{frequency: .2f}')
