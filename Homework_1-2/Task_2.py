# a) Дано целое число. Если оно является положительным, то прибавить к нему 1;
# в противном случае вычесть из него 2. Вывести полученное число.
num = int(input("Введите целое число: "))
if num > 0:
    result_a = num + 1
else:
    result_a = num - 2
print(f"Результат: {result_a}")

# б) Даны три числа. Вывести вначале наименьшее, а затем наибольшее из данных чисел.
num1 = float(input("Введите первое число: "))
num2 = float(input("Введите второе число: "))
num3 = float(input("Введите третье число: "))

if num1 <= num2 and num1 <= num3:
    minimum = num1
elif num2 <= num1 and num2 <= num3:
    minimum = num2
else:
    minimum = num3

if num1 >= num2 and num1 >= num3:
    maximum = num1
elif num2 >= num1 and num2 >= num3:
    maximum = num2
else:
    maximum = num3

print(f"Наименьшее число: {minimum}")
print(f"Наибольшее число: {maximum}")

"""
Билет на одну поездку в метро стоит 15 рублей, 
билет на 5 поездок стоит 70 рублей, 
билет на 10 поездок стоит 125 рублей, 
билет на 20 поездок стоит 230 рублей, 
билет на 60 поездок стоит 440 рублей.

Задача: определить минимальную стоимость билетов для n поездок, 
чтобы суммарное количество поездок было не меньше n.
"""


required_trips = int(input("Введите необходимое количество поездок: "))

num_60 = required_trips // 60
left = required_trips % 60

num_20 = num_10 = num_5 = num_1 = 0

if left >= 36:
    num_60 += 1
else:
    if left == 0:
        pass
    elif 1 <= left <= 4:
        num_1 = left
    elif left == 5:
        num_5 = 1
    elif 6 <= left <= 8:
        num_5 = 1
        num_1 = left - 5
    elif 9 <= left <= 10:
        num_10 = 1
    elif 11 <= left <= 14:
        num_10 = 1
        num_1 = left - 10
    elif left == 15:
        num_10, num_5 = 1, 1
    elif 16 <= left <= 17:
        num_10, num_5 = 1, 1
        num_1 = left - 15
    elif 18 <= left <= 20:
        num_20 = 1
    elif 21 <= left <= 24:
        num_20 = 1
        num_1 = left - 20
    elif left == 25:
        num_20, num_5 = 1, 1
    elif 26 <= left <= 28:
        num_20, num_5 = 1, 1
        num_1 = left - 25
    elif 29 <= left <= 30:
        num_20, num_10 = 1, 1
    elif 31 <= left <= 34:
        num_20, num_10 = 1, 1
        num_1 = left - 30
    elif left == 35:
        num_20, num_10, num_5 = 1, 1, 1

total_cost = (
    num_60 * 440 +
    num_20 * 230 +
    num_10 * 125 +
    num_5 * 70 +
    num_1 * 15
)

print(f"Билетов на 60: {num_60}")
print(f"Билетов на 20: {num_20}")
print(f"Билетов на 10: {num_10}")
print(f"Билетов на 5: {num_5}")
print(f"Билетов на 1: {num_1}")
print(f"Общая стоимость: {total_cost} руб.")