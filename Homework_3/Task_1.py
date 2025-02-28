"""
a) Числа Армстронга: Напишите программу, которая находит все числа Армстронга в диапазоне от 1 до N.
Число Армстронга — это такое число, которое равно сумме своих цифр, возведенных в степень, равную количеству цифр этого числа.
Например: Для числа 153: 1^3+5^3+3^3=153, значит 153 — число Армстронга.
"""
limit = int(input("Введите число N, до которого нужно искать числа Армстронга: "))

print(f"Числа Армстронга в диапазоне от 1 до {limit}:")

for num in range(1, limit + 1):
    digits_count = 0  
    temp_num = num  

    while temp_num > 0:
        digits_count += 1
        temp_num //= 10  

    powers_sum = 0
    temp_num = num  

    while temp_num > 0:
        digit = temp_num % 10  
        digit_power = digit ** digits_count  
        powers_sum += digit_power  
        temp_num //= 10  

    if powers_sum == num:
        print(f"{num}")
"""
б) Факториал: Вычислите N! ("эн-факториал") – произведение всех натуральных чисел от 1 до N ( N!=1∙2∙3∙…∙ N ). 
Пример: Ввод: 3 Вывод: 6
"""

num = int(input("Введите число для вычисления его факториала: "))
factorial = 1
while num>0:
    factorial =  factorial *  num
    num -= 1
print(factorial)

"""
c) Выведите все натуральные делители числа x в порядке возрастания (включая 1 и само число).
Ввод	Вывод
32	    1 2 4 8 16 32
"""

num = int(input("Введите число для поиска делителей: "))
for divisor in range(1, num + 1):
    if num % divisor == 0:
        print(divisor)
