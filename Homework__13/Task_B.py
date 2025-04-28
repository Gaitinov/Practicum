
"""
Вариант 2

b) Класс Patient
Создайте класс Patient с инкапсуляцией полей: имя, ИИН, диагноз, температура. Диагноз может изменяться только через метод update_diagnosis(doctor_id). Температура задаётся через property, если выше 39°C — выводится предупреждение.
"""

class Patient:
    # Конструктор: инициализация пациента.
    def __init__(self, name: str, iin: str, diagnosis: str, temperature: float):
        # Использование двойного подчеркивания для name mangling (или одинарного как соглашение).
        self.__name = name
        self.__iin = iin
        self.__diagnosis = diagnosis
        # Вызов сеттера для начальной установки и проверки.
        self.temperature = temperature

    # Свойство (property) для чтения имени. Setter не определен - только чтение снаружи.
    @property
    def name(self) -> str:
        return self.__name

    # Свойство (property) для чтения ИИН. Setter не определен - только чтение снаружи.
    @property
    def iin(self) -> str:
        return self.__iin

    # Свойство (property) для чтения диагноза. Setter не определен - только чтение снаружи.
    @property
    def diagnosis(self) -> str:
        return self.__diagnosis

    # Метод для контролируемого обновления диагноза (инкапсуляция).
    def update_diagnosis(self, new_diagnosis: str, doctor_id: str):
        self.__diagnosis = new_diagnosis # Прямое изменение внутреннего поля.

    # Свойство (property) для чтения температуры.
    @property
    def temperature(self) -> float:
        return self.__temperature

    # Сеттер для свойства temperature, выполняется при присваивании значения.
    @temperature.setter
    def temperature(self, value: float):
        if value > 39.0:
            print(f"[ПРЕДУПРЕЖДЕНИЕ] У пациента {self.name} температура {value}°C, что выше 39°C!")
        self.__temperature = value

    # Метод для получения форматированной информации о пациенте.
    def get_info(self) -> str:
        return f"Имя: {self.name}, ИИН: {self.iin}, Диагноз: {self.diagnosis}, Температура: {self.temperature:.1f}°C"

# Демонстрация работы класса Patient).
if __name__ == "__main__":
    # Создание пациента (сработает сеттер температуры в __init__).
    patient1 = Patient(name="Живой Человек", iin="910203300400", diagnosis="Грипп", temperature=40.0)
    print("Результат создания:")
    print(patient1.get_info()) # Вывод информации через метод.

    print("Чтение атрибутов через property:")
    print(f"  Имя: {patient1.name}")
    print(f"  Диагноз: {patient1.diagnosis}")

    print("Обновление диагноза через метод:")
    patient1.update_diagnosis("Здоров", doctor_id="DR456")
    print(patient1.get_info())

    print("Обновление температуры через property setter:")
    patient1.temperature = 36.6 # Установка нормальной температуры (без предупреждения).
    print(f"  Новая температура: {patient1.temperature}")
    patient1.temperature = 39.2 # Установка высокой температуры (с предупреждением).
    print(f"  Еще новая температура: {patient1.temperature}")
    print(patient1.get_info())

    print("Попытка прямого изменения диагноза (вызовет ошибку):")
    try:
        patient1.diagnosis = "Простуда"
    except AttributeError as e:
        print(f"  (Ожидаемая ошибка: {e})")