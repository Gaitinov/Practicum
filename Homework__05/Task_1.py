import random

"""
a) Объединение словарей с суммированием значений:
Даны два словаря. Если ключи совпадают, их значения нужно сложить.
Ввод: {'a': 10, 'b': 20}, {'b': 5, 'c': 15}
Вывод: {'a': 10, 'b': 25, 'c': 15}
"""
print("# a) Объединение словарей с суммированием значений. Если ключи совпадают, их значения нужно сложить.")
dict_a1 = {'a': 10, 'b': 20}
dict_a2 = {'b': 5, 'c': 15}

result_a = {}
for key in dict_a1:
    result_a[key] = dict_a1[key]
for key in dict_a2:
    if key in result_a:
        result_a[key] = result_a[key] + dict_a2[key]
    else:
        result_a[key] = dict_a2[key]

print(f"Вывод: {result_a}")


"""
б) Частота элементов в кортеже:
Дан кортеж чисел. Нужно вернуть словарь с частотой каждого числа.
Ввод: (1, 2, 2, 3, 3, 3)
Вывод: {1: 1, 2: 2, 3: 3}
"""
print("# б) Частота элементов в кортеже:")
tuple_b = (1, 2, 2, 3, 3, 3)

counts_b = {}
for num in tuple_b:
    if num in counts_b:
        counts_b[num] = counts_b[num] + 1
    else:
        counts_b[num] = 1

result_b = counts_b
print(f"Вывод: {result_b}")


"""
c) Поиск самого длинного ключа в словаре:
Дан словарь с строковыми ключами. Найти ключ с наибольшей длиной.
Ввод: {'apple': 5, 'banana': 3, 'watermelon': 7}
Вывод: 'watermelon'
"""
print("# c) Поиск самого длинного ключа в словаре:")
dict_c = {'apple': 5, 'banana': 3, 'watermelon': 7}

max_length_key = ''
for key in dict_c:
    if len(key) > len(max_length_key):
        max_length_key = key

result_c = max_length_key
print(f"Вывод: '{result_c}'")


"""
d) Перемешивание кортежа:
Дан кортеж. Нужно случайным образом перемешать его элементы.
Ввод: (1, 2, 3, 4, 5)
Вывод: (например) (3, 1, 5, 2, 4)
"""
print("# d) Перемешивание кортежа:")
tuple_d = (1, 2, 3, 4, 5)

list_d = list(tuple_d)
random.shuffle(list_d)
result_d = tuple(list_d)

print(f"Вывод: {result_d}")
random.shuffle(list_d)
result_d = tuple(list_d)

print(f"Вывод: {result_d}")

"""
e) Разбиение словаря на кортежи:
Дан словарь. Преобразовать его в список кортежей (ключ, значение).
Ввод: {'x': 10, 'y': 20, 'z': 30}
Вывод: [('x', 10), ('y', 20), ('z', 30)]
"""
print("# e) Разбиение словаря на кортежи:")
dict_e = {'x': 10, 'y': 20, 'z': 30}

result_e = []
for key in dict_e:
    result_e = result_e + [(key, dict_e[key])]

print(f"Вывод: {result_e}")