"""
a) НОД двух чисел:
Напишите функцию gcd(a, b), которая принимает два числа a и b и возвращает их наибольший общий делитель.
Ввод: 12 18
Вывод: 6
"""
print("# a) НОД двух чисел:")
def gcd(a, b): #  Это алгоритм Евклида, при том работает при любом случае 12 - 18 или 18 - 12
    while b: # это пока b не равен нулю
        a, b = b, a % b
    return a

print("Введите два числа через пробел (например, 12 18):")
a, b = map(int, input().split())
result_a = gcd(a, b)
print(f"Ввод: {a} {b}")
print(f"Вывод: {result_a}")


"""
б) Следующее простое число:
Напишите функцию next_prime(n), которая принимает число n и возвращает следующее простое число, большее или равное n.
Ввод: 10
Вывод: 11
"""
print("# б) Следующее простое число:")
def is_prime(num):
    if num < 2: # Простые числа от  должны быть больше 1
        return False
    for i in range(2, int(num ** 0.5) + 1): # быстрый способ проверить простое ли число
        if num % i == 0:
            return False
    return True

def next_prime(n):
    num = n
    while True: # бесконечный цикл
        if is_prime(num):
            return num
        num += 1

print("Введите число (например, 10):")
n = int(input())
result_b = next_prime(n)
print(f"Ввод: {n}")
print(f"Вывод: {result_b}")


"""
c) Число Фибоначчи:
Напишите функцию fibonacci(n), которая возвращает n-е число Фибоначчи.
Ввод: 5
Вывод: 5
"""
print("# c) Число Фибоначчи:")
def fibonacci(n):
    if n <= 0:
        return 0
    elif n == 1:
        return 1
    a, b = 0, 1 #  значения для начала чисел Фибоначчи
    for _ in range(2, n + 1): # просто до n
        a, b = b, a + b  #  вычисление  следующее числа Фибоначчи
    return b

print("Введите номер числа Фибоначчи (например, 5):")
n = int(input())
result_c = fibonacci(n)
print(f"Ввод: {n}")
print(f"Вывод: {result_c}")
