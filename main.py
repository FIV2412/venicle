def validate_fuel_consumption(method):
    """Декоратор для проверки условий перед расчётом расхода топлива."""
    def wrapper(self, value):
        if value < 0:
            print("Ошибка: значение не может быть отрицательным.")
            return None

        result = method(self, value)
        if result is None:
            return None

        if result > self._current_fuel_level:
            print(f"Ошибка: недостаточно топлива для поездки. Нужно {result} л, в наличии {self._current_fuel_level} л.")
            return None

        self._current_fuel_level -= result
        return result

    return wrapper

    
class Vehicle:
    """
    Базовый класс для транспортных средств.
    """
    def __init__(self, name, fuel_tank_capacity):
        
        """Инициализирует транспортное средство с заданным названием и вместимостью бака."""
        self._name = name
        self._fuel_tank_capacity = fuel_tank_capacity
        self._current_fuel_level = fuel_tank_capacity

    def refuel(self, amount):
        """
        Заправка транспортного средства.
        """
        if amount <= 0:
            print("Ошибка: количество топлива должно быть положительным.")
            return         # что сюда?    
        if self._current_fuel_level + amount > self._fuel_tank_capacity:
            print("Ошибка: превышение вместимости топливного бака.")
            return

        self._current_fuel_level += amount
        print(f"Заправлено {amount} л. Текущий уровень: {self._current_fuel_level} л.")    
            
    def display_info(self):
        """
        Отображает основную информацию о транспортном средстве.
        """
        print(f"Название: {self._name}, Вместимость бака: {self._fuel_tank_capacity} л, Текущий уровень топлива: {self._current_fuel_level} л.")


class Car(Vehicle):
    """
    Класс для представления автомобиля.
    Наследует от Vehicle."""
    def __init__(self, name, fuel_tank_capacity, fuel_consumption_per_100km):
        """Инициализирует автомобиль."""
        super().__init__(name, fuel_tank_capacity)
        self._fuel_consumption_per_100km = fuel_consumption_per_100km
    @validate_fuel_consumption    
    def calculate_fuel_consumption(self, distance):
    
            result = (distance / 100)*self._fuel_consumption_per_100km
            print(f"Расход на {distance} км: {round(result,2)} л.")
    
            return result

class Airplane(Vehicle):
    """
    Класс для представления самолёта.
    Наследует от Vehicle.
    """
    def __init__(self, name, fuel_tank_capacity, fuel_consumption_per_hour):
            """Инициализирует самолет."""
            super().__init__(name, fuel_tank_capacity)
            self._fuel_consumption_per_hour = fuel_consumption_per_hour
    @validate_fuel_consumption
    def calculate_fuel_consumption(self, flight_time):
    
            result = flight_time * self._fuel_consumption_per_hour
            print(f"Расход за {flight_time} ч: {round(result,2)} л.")
    
            return result

class Boat(Vehicle):
    """
    Класс для представления катера.
    Наследует от Vehicle.
    """
    def __init__(self, name, fuel_tank_capacity, fuel_consumption_per_hour):
        """Инициализирует катер."""
        super().__init__(name, fuel_tank_capacity)
                
        self._fuel_consumption_per_hour = fuel_consumption_per_hour
    @validate_fuel_consumption    
    def calculate_fuel_consumption(self, travel_time):
        
       result = travel_time * self._fuel_consumption_per_hour
       print(f"Расход за {travel_time} ч: {round(result,2)} л.")
        
       return result


# Создание объектов
car = Car("Toyota Camry", 60, 8)
airplane = Airplane("Boeing 737", 20000, 2500)
boat = Boat("Sea Ray", 150, 30)

# Отображение информации
car.display_info() # Название: Toyota Camry, Вместимость бака: 60 л, Текущий уровень топлива: 60 л.
airplane.display_info() # Название: Boeing 737, Вместимость бака: 20000 л, Текущий уровень топлива: 20000 л.
boat.display_info() # Название: Sea Ray, Вместимость бака: 150 л, Текущий уровень топлива: 150 л.

# Заправка транспортных средств
car.refuel(30) # Ошибка: превышение вместимости топливного бака.
airplane.refuel(10000) # Ошибка: превышение вместимости топливного бака.
boat.refuel(80) # Ошибка: превышение вместимости топливного бака.

# Расчёт расхода топлива
car.calculate_fuel_consumption(150) # Расход на 150 км: 12.00 л.
airplane.calculate_fuel_consumption(3) # Расход за 3 ч: 7500.00 л.
boat.calculate_fuel_consumption(2) # Расход за 2 ч: 60.00 л.
