"""
Вариант 2
Задача про фигуры

Создайте базовый класс Shape, представляющий геометрическую фигуру:
- Метод GetArea() — должен быть абстрактным (в Python можно выбросить NotImplementedError).
- Метод GetInfo() — возвращает тип фигуры.

Создайте производный класс Rectangle:
- Свойства: ширина (Width) и высота (Height)
- Реализуйте методы GetArea() и GetInfo()

Также создайте класс Circle:
- Свойство: радиус (Radius)
- Реализуйте методы GetArea() и GetInfo()

Добавить комментарии к каждой строке кода
"""

import math  # Импорт модуля math для pi


# Объявление класса Shape
class Shape:
    # Определение метода GetArea (абстрактный)
    def GetArea(self):
        # Исключение NotImplementedError используется для обозначения абстрактного метода
        # чтобы напомнить о необходимости реализации в подклассе
        raise NotImplementedError("Метод GetArea должен быть реализован в подклассе")
    # Определение метода GetInfo
    def GetInfo(self):
        return "Shape"

# Объявление класса Rectangle (наследование от Shape)
class Rectangle(Shape):
    # Определение конструктора класса Rectangle
    def __init__(self, width, height):
        self.Width = width  # Атрибут ширины
        self.Height = height  # Атрибут высоты

    # Определение метода GetArea (прямоугольник)
    def GetArea(self):
        return self.Width * self.Height

    # Определение метода GetInfo (прямоугольник)
    def GetInfo(self):
        return "Rectangle"

# Объявление класса Circle (наследование от Shape)
class Circle(Shape):
    # Определение конструктора класса Circle
    def __init__(self, radius):
        self.Radius = radius  # Атрибут радиуса

    # Определение метода GetArea (круг)
    def GetArea(self):
        return math.pi * (self.Radius ** 2)

    # Определение метода GetInfo (круг)
    def GetInfo(self):
        return "Circle"

# Проверка работоспособности классов
if __name__ == "__main__":  # Блок кода выполняется только при запуске файла напрямую
    rect = Rectangle(3, 4)  # Создание прямоугольника со сторонами 3 и 4
    print(f"Rectangle: площадь = {rect.GetArea()}, тип = {rect.GetInfo()}")

    circ = Circle(5)  # Создание круга с радиусом 5
    print(f"Circle: площадь = {circ.GetArea():.2f}, тип = {circ.GetInfo()}")
