"""
Вариант 2: Задача про магазин

Создайте класс Product, который описывает продукт в магазине:
•	Название товара (Name).
•	Цена (Price).
•	Количество на складе (Stock).
Создайте два конструктора:
1.	Один принимает все параметры.
2.	Второй принимает только название товара, а цена и количество по умолчанию устанавливаются в 0.
Добавьте методы:
•	UpdatePrice(decimal newPrice) — обновляет цену товара.
•	Restock(int quantity) — пополняет запас товара на складе.
•	GetProductInfo() — возвращает строку с информацией о товаре.
•	Sell(int quantity) — уменьшает запас на складе при продаже.

"""

class Product:
    # Конструктор с параметрами, передача позволяет при создании указать только название или все параметры
    def __init__(self, name, price=0.0, stock=0): # self нужен чтобы было корректное обращение к определенному объекту
        self.name = name  # self нужно чтобы указать, что это именно  к текущему объекту относится
        self.price = price
        self.stock = stock

    # Методы позволяют, например, задать корректные проверки на ввод данных, чтобы их каждый раз не писать.
    def update_price(self, new_price):
        self.price = new_price

    def restock(self, quantity):
        if quantity > 0:  # Дополнительная проверочка, в sell аналогично
            self.stock = self.stock + quantity
            print(f"{quantity} штук добавлено на склад.")
        else:
            print(f"Нельзя добавить {quantity} штук (количество должно быть больше нуля).")

    def get_product_info(self):
        info_str = f"Товар: {self.name}, Цена: {self.price}, На складе: {self.stock}"
        return info_str

    def sell(self, quantity):
        if quantity > 0:
            if self.stock >= quantity:
                self.stock = self.stock - quantity
                print(f"{quantity} штук товара '{self.name}' продано!")
            else:
                print(f"Не хватает товара '{self.name}' на складе! (нужно {quantity}, есть {self.stock})")
        else:
            print(f"Нельзя продать {quantity} штук (количество должно быть больше нуля).")

print("--- Создание ---")
item1 = Product("Ручка")
print(item1.get_product_info())

item2 = Product("Тетрадь", 50.0, 100)
print(item2.get_product_info())


print("\n--- Обновление и пополнение ---")
item1.update_price(15.5)
print("Ручка после обновления цены:", item1.get_product_info())

item1.restock(50)
print("Ручка после пополнения:", item1.get_product_info())

item2.restock(0)
print("Тетради после попытки пополнить на 0:", item2.get_product_info())

item2.restock(-10)
print("Тетради после попытки пополнить на -10:", item2.get_product_info())

print("\n--- Продажа ---")
item1.sell(10)
print("Ручки после продажи 10 шт:", item1.get_product_info())

item2.sell(30)
print("Тетради после продажи 30 шт:", item2.get_product_info())

item1.sell(50)
print("Ручки после попытки продать 50 шт:", item1.get_product_info())

item2.sell(0)
print("Тетради после попытки продать 0 шт:", item2.get_product_info())

item2.sell(-5)
print("Тетради после попытки продать -5 шт:", item2.get_product_info())