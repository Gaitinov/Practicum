"""
a) Удаление элементов, которые встречаются только один раз:
Дан список чисел, удалите из него все элементы, которые встречаются только один раз.
Ввод: [4, 3, 5, 3, 4, 4, 7, 8]
Вывод: [4, 3, 3, 4, 4]
"""
print("# a) Удаление элементов, которые встречаются только один раз:")
str_a = input("Введите список чисел, например: [4, 3, 5, 3, 4, 4, 7, 8]: ")
list_a = eval(str_a)

counts_a = {}
for num in list_a:
    if num in counts_a:
        counts_a[num] = counts_a[num] + 1
    else:
        counts_a[num] = 1

result_a = []
for num in list_a:
    if counts_a[num] > 1:
        result_a = result_a + [num]

print(f"Вывод: {result_a}")


"""
б) Наибольшая последовательность подряд идущих одинаковых чисел:
Напишите функцию, которая принимает список чисел и возвращает наибольшую последовательность подряд идущих одинаковых чисел в этом списке.
Если таких последовательностей несколько, вернуть первую.
Ввод: [1, 2, 2, 2, 3, 3, 4, 4, 4, 4, 5]
Вывод: [4, 4, 4, 4]
"""
print("# б) Наибольшая последовательность подряд идущих одинаковых чисел:")
str_b = input("Введите список чисел, например: [1, 2, 2, 2, 3, 3, 4, 4, 4, 4, 5]: ")
list_b = eval(str_b)

if not list_b:
    result_b = []
else:
    max_seq_b = []
    current_seq_b = []
    current_num_b = list_b[0]
    current_seq_b = [current_num_b]

    for i in range(1, len(list_b)):
        num_b = list_b[i]
        if num_b == current_num_b:
            current_seq_b = current_seq_b + [num_b]
        else:
            if len(current_seq_b) > len(max_seq_b):
                max_seq_b = current_seq_b
            current_seq_b = [num_b]
            current_num_b = num_b

    if len(current_seq_b) > len(max_seq_b):
        max_seq_b = current_seq_b

    result_b = max_seq_b

print(f"Вывод: {result_b}")


"""
c) Сортировка списка по количеству вхождений элементов:
Дан список чисел. Отсортируйте его так, чтобы элементы с большим количеством вхождений шли раньше элементов с меньшим количеством вхождений.
При равном количестве вхождений сохранить их исходный порядок.
Ввод: [4, 3, 3, 2, 2, 2, 1]
Вывод: [2, 2, 2, 3, 3, 4, 1]
"""
print("# c) Сортировка списка по количеству вхождений элементов:")
str_c = input("Введите список чисел, например: [4, 3, 3, 2, 2, 2, 1]: ")
list_c = eval(str_c)

counts_c = {}
for num in list_c:
    if num in counts_c:
        counts_c[num] = counts_c[num] + 1
    else:
        counts_c[num] = 1

unique_elements_c = []
processed_elements_c = []

for num in list_c:
    if num not in processed_elements_c:
        unique_elements_c = unique_elements_c + [num]
        processed_elements_c = processed_elements_c + [num]
sorted_list_c = []
while unique_elements_c:
    max_count_element = unique_elements_c[0]
    for element in unique_elements_c:
        if counts_c[element] > counts_c[max_count_element]:
            max_count_element = element

    sorted_list_c_temp = []
    for _ in range(counts_c[max_count_element]):
        sorted_list_c_temp = sorted_list_c_temp + [max_count_element]
    sorted_list_c = sorted_list_c + sorted_list_c_temp

    next_unique_elements_c = []
    for element in unique_elements_c:
        if element != max_count_element:
            next_unique_elements_c = next_unique_elements_c + [element]
    unique_elements_c = next_unique_elements_c

print(f"Вывод: {sorted_list_c}")
