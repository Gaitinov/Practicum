"""
№112393. Самая длинная цепочка
Найти длину самой длинной цепочки одинаковых чисел, идущих подряд в файле input.txt . 
Количество чисел неизвестно. Результат записать в файл output.txt .

Входные данные
Целые числа записаны в файле input.txt в столбик, по одному в строке. 
Ввод заканчивается тогда, когда заканчиваются данные в файле.

Выходные данные
Программа должна вывести в файл output.txt длину самой длинной цепочки одинаковых чисел, идущих подряд.

Примеры
Входные данные (файл input.txt):
1
5
5
2
3
Выходные данные (файл output.txt):
2
"""

max_length = 0      # максимальная длина цепочки
current_length = 0  # нынешняя длина цепочки
previous_num = None # предыдущее число

with open("input_chain.txt", "r") as infile:  # открытие файла для чтения
    for line in infile:  # чтение файла построчно
        current_num = int(line.strip())  # преобразование строки в целое число
        if current_num == previous_num:  # сравнение с предыдущим числом
            current_length += 1  # увеличение длины цепочки
        else:
            if current_length > max_length:  # если число изменилось - сравнение длины цепочки
                max_length = current_length
            current_length = 1  # сброс длины цепочки
            previous_num = current_num  # обновление предыдущего числа

if current_length > max_length:  # после окончания ещё раз проверка
    max_length = current_length

result = str(max_length)

with open("output_chain.txt", "w") as outfile:  # открытие файла для записи
    outfile.write(result)
