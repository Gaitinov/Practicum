"""
Вариант 2

c) Класс DeliveryService
Реализуйте базовый класс DeliveryService с методом calculate_cost(weight_kg, distance_km). 
Создайте классы StandardDelivery, ExpressDelivery, EcoDelivery с разной логикой расчёта стоимости доставки.
"""

from abc import ABC, abstractmethod

class DeliveryService(ABC):
    @abstractmethod
    def calculate_cost(self, weight_kg: float, distance_km: float) -> float: # Стрелочка указывает на возвращаемое значение
        raise NotImplementedError("Метод calculate_cost должен быть реализован в подклассе")

# Класс для стандартной доставки.
class StandardDelivery(DeliveryService):
    def calculate_cost(self, weight_kg: float, distance_km: float) -> float:
        base_rate = 500 # базовая ставка
        cost = base_rate + (weight_kg * 100) + (distance_km * 10)
        return cost

# Класс для экспресс-доставки.
class ExpressDelivery(DeliveryService):
    def calculate_cost(self, weight_kg: float, distance_km: float) -> float:
        base_rate = 1000 # повышенная базовая ставка
        cost = base_rate + (weight_kg * 200) + (distance_km * 25)
        return cost

# Класс для эко-доставки.
class EcoDelivery(DeliveryService):
    def calculate_cost(self, weight_kg: float, distance_km: float) -> float:
        if weight_kg > 10:
            raise ValueError("EcoDelivery не поддерживает посылки тяжелее 10 кг!")
        base_rate = 300 # низкая базовая ставка
        cost = base_rate + (weight_kg * 50) + (distance_km * 8)
        return cost

# Демонстрация работы классов доставки.
if __name__ == "__main__":
    deliveries = [
        StandardDelivery(),
        ExpressDelivery(),
        EcoDelivery()
    ]
    # Параметры посылки для теста.
    weight = 5.0
    distance = 100.0

    print(f"Расчет стоимости для {weight} кг на {distance} км:")
    # Демонстрация полиморфизма: перебор списка и вызов одного и того же метода.
    for service in deliveries:
        service_type = type(service).__name__ # Получение имени класса для вывода.
        try:
            price = service.calculate_cost(weight, distance)
            print(f"  {service_type}: {price:.2f} тг")
        except ValueError as e: #  Здесь должна быть конкретная ошибка ValueError, которая может быть вызвана в EcoDelivery.
            print(f"  {service_type}: Ошибка - {e}")

    # Отдельная проверка случая, который должен вызвать ошибку в EcoDelivery.
    print("EcoDelivery с весом 15 кг (должна быть ошибка):")
    try:
        eco_service = EcoDelivery()
        heavy_weight = 15.0
        price = eco_service.calculate_cost(heavy_weight, 50) # Попытка расчета с большим весом.
        print(f"  EcoDelivery: {price:.2f} тг") # Этот код не должен выполниться.
    except ValueError as e:
        print(f"  EcoDelivery: Ошибка - {e}") 