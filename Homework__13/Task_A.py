
"""
Вариант 2 
ПРИМЕЧАНИЕ: Все задачи должны быть решены с использованием объектно-ориентированного подхода на языке Python.
Необходимо следить за корректной реализацией принципов инкапсуляции, использования @property и полиморфизма. 
a) Класс Metric
Создайте абстрактный класс Metric с property value и is_critical. 
Создайте наследников CPUMetric, RAMMetric, DiskMetric с разной логикой получения метрик и порогов

"""

# Основа для всех метрик - ABC и abstractmethod, чтобы установить структуру - 
# обязательное наличие свойств 'value' и 'is_critical' у всех наследников.
from abc import ABC, abstractmethod
# random, чтобы имитировать данные,
import random

# Абстрактный базовый класс. Наследники ОБЯЗАНЫ будут реализовать абстрактные свойства.
class Metric(ABC):
    # ОБЯЗАТЕЛЬНОЕ свойство: каждая метрика-наследник должна реализовать способ получения своего значения.
    # @property обеспечивает удобный доступ (metric.value), @abstractmethod гарантирует реализацию в подклассах.
    @property
    @abstractmethod
    def value(self):
        """Абстрактное свойство для получения текущего значения метрики.
        Определение этого свойства в подклассе является обязательным. """
        raise NotImplementedError("Свойство value должно быть реализовано в подклассе")

    # ОБЯЗАТЕЛЬНОЕ свойство: каждая метрика должна определять, является ли её состояние критическим.
    # Комбинация @property и @abstractmethod обеспечивает единообразный интерфейс проверки статуса (metric.is_critical).
    @property
    @abstractmethod
    def is_critical(self):
        """Абстрактное свойство для определения, является ли текущее значение метрики критическим.
        Определение этого свойства в подклассе также является обязательным. """
        raise NotImplementedError("Свойство is_critical должно быть реализовано в подклассе")

    # Общий метод для всех метрик: предоставляет стандартный способ получения сводной информации.
    # Работает для любого наследника Metric благодаря полиморфизму.
    def get_info(self):
        """Возвращение общей информации о метрике.
        Обращение к свойству value текущего объекта приведет к выполнению реализации из дочерних классов. """
        current_value = self.value
        # Аналогично для is_critical
        critical_status = self.is_critical
        return f"Значение: {current_value:.2f}, Критическое: {critical_status}" # Возвращение строки с информацией о метрике.
    
class CPUMetric(Metric):
    # Конструктор с параметрами порога и начального значения для имитации.
    def __init__(self, critical_threshold=90.0):
        # Сохранение порога для последующего сравнения в is_critical.
        self._critical_threshold = critical_threshold
        # Рандомное значение
        self._simulated_value = random.uniform(0.0, 100.0)

    @property
    def value(self):
        # Симулирует получение текущей загрузки CPU в процентах."""
        change = random.uniform(-5.0, 5.0)
        # Обновление внутреннего состояния симуляции с гарантией нахождения значения в пределах [0, 100].
        self._simulated_value = max(0.0, min(100.0, self._simulated_value + change))
        # Возврат актуального симулированного значения.
        return self._simulated_value

    @property
    def is_critical(self):
        # Cравнение текущего симулированного значения CPU (полученного через self.value) с порогом.
        return self.value >= self._critical_threshold

class RAMMetric(Metric):
    # Конструктор для RAM.
    def __init__(self, critical_threshold=85.0):
        # Критичное значение для RAM.
        self._critical_threshold = critical_threshold
        # Начальное значение симуляции для RAM.
        self._simulated_value = random.uniform(20.0, 90.0)


    @property
    def value(self):
        # Логика симуляции для RAM.
        change = random.choice([-1, -0.5, 0, 0.5, 1, 1.5, 2]) * random.uniform(0.5, 1.5)
        # Обновление  состояния с удержанием в пределах [0, 100].
        self._simulated_value = max(0.0, min(100.0, self._simulated_value + change))
        # Возврат текущего симулированного значения RAM.
        return self._simulated_value

    @property
    def is_critical(self):
        # Сравнение текущего значения RAM (self.value) с её порогом.
        return self.value >= self._critical_threshold

class DiskMetric(Metric):
    # Конструктор задание метки диска.
    def __init__(self, disk_label='C:', critical_threshold=95.0):
        # Метка диска полезна для нескольких DiskMetric объектов.
        self._disk_label = disk_label
        # Порог критичности для диска.
        self._critical_threshold = critical_threshold
        # Начальное симулированное значение заполненности диска.
        self._simulated_value = random.uniform(10.0, 80.0)

    @property
    def value(self):
        # Логика симуляции для Disk: имитация медленного заполнения диска небольшими случайными приращениями.
        increase = random.uniform(0.01, 0.1)
        # Обновление значения с ограничением до 100%.
        self._simulated_value = min(100.0, self._simulated_value + increase)
        # Возврат текущего симулированного значения заполненности диска.
        return self._simulated_value

    @property
    def is_critical(self):
        # Сравнение текущего значения заполненности (self.value) с порогом для диска."""
        return self.value >= self._critical_threshold

# Для демонстрации работы классов и ООП.
if __name__ == "__main__":
    cpu_metric = CPUMetric(critical_threshold=90.0)
    ram_metric = RAMMetric(critical_threshold=85.0)
    disk_metric_d = DiskMetric(disk_label='D:', critical_threshold=95.0)
    for i in range(3):
        # Вызов get_info() для каждого объекта. Внутри get_info() используются свойства .value и .is_critical.  
        print(f"  CPU: {cpu_metric.get_info()}")
        print(f"  RAM: {ram_metric.get_info()}")
        print(f"  Диск {disk_metric_d._disk_label}: {disk_metric_d.get_info()}")

    metrics_list = [cpu_metric, ram_metric, disk_metric_d]
    for one_metric in metrics_list: 
        metric_type = type(one_metric).__name__ 
        # Вызов одного и того же метода get_info() для объектов разных типов.
        # Python сам подставит нужные реализации .value и .is_critical внутри get_info().
        print(f"Информация от {metric_type}: {one_metric.get_info()}")
