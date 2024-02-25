if __name__ == "__main__":
    class Automobiles:
        """
        Базовый класс "Автомобили"
        """

        def __init__(self, brand: str, model: str, year: int):
            """
            Конструктор класса Автомобили.

            :param brand: Марка автомобиля
            :param model: Модель автомобиля
            :param year: Год выпуска автомобиля
            """
            self.brand = brand
            self.model = model
            self.year = year

        def __str__(self) -> str:
            """
            Метод для получения строкового представления объекта.

            :return: Строковое представление объекта
            """
            return f"{self.brand} {self.model} ({self.year})"

        def __repr__(self) -> str:
            """
            Метод для получения представления объекта в виде строки.

            :return: Представление объекта в виде строки
            """
            return self.__str__()

        def launch(self) -> str:
            """
            Метод для запуска транспортного средства.

            :return: Сообщение о запуске транспортного средства
            """
            return "Транспортное средство запущено!"


    class PassengerCar(Automobiles):
        """
        Дочерний класс "Легковая машина"
        """

        def __init__(self, brand: str, model: str, year: int, body_type: str):
            """
            Конструктор класса Легковая машина.

            :param brand: Марка автомобиля
            :param model: Модель автомобиля
            :param year: Год выпуска автомобиля
            :param body_type: Тип кузова автомобиля
            """
            super().__init__(brand, model, year)
            self.body_type = body_type

        def launch(self) -> str:
            """
            Перегруженный метод для запуска легкового автомобиля.

            :return: Сообщение о запуске легкового автомобиля
            """
            return f"Легковой автомобиль запущен! Тип кузова: {self.body_type}"

        def refuel(self, fuel_amount: float) -> str:
            """
            Метод для заправки легкового автомобиля.

            :param fuel_amount: Количество заправляемого топлива (в литрах)
            :return: Сообщение о заправке легкового автомобиля
            """
            return f"Легковой автомобиль заправлен на {fuel_amount} литров."

    class Truck(Automobiles):
        """
        Дочерний класс "Грузовая машина"
        """

        def __init__(self, brand: str, model: str, year: int, lifting_capacity: str):
            """
            Конструктор класса Грузовая машина.

            :param brand: Марка автомобиля
            :param model: Модель автомобиля
            :param year: Год выпуска автомобиля
            :param lifting_capacity: Грузоподъемность автомобиля
            """
            super().__init__(brand, model, year)
            self.lifting_capacity = lifting_capacity

        def launch(self) -> str:
            """
            Перегруженный метод для запуска грузового автомобиля.

            :return: Сообщение о запуске грузового автомобиля
            """
            return f"Грузовой автомобиль запущен! Грузоподъемность: {self.lifting_capacity}"


    if __name__ == "__main__":
        car = PassengerCar("Audi", "A6", 2022, "Седан")
        print(car)  # Выводит Audi A6 (2022)
        print(car.launch())  # Выводит: Легковой автомобиль запущен!
        print(car.refuel(50))  # Выводит: Легковой автомобиль заправлен на 50 литров.
    if __name__ == "__main__":
        car2 = Truck("Ford", "Transit 310", 2021, "1200 кг")
        print(car2)  # Выводит Ford Transit 310 (2021)
        print(car2.launch())  # Выводит: Грузовой автомобиль запущен!
    pass
