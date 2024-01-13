# TODO Написать 3 класса с документацией и аннотацией типов
import doctest


class Numizmat:
    """
    Класс, представляющий монету.

    Атрибуты:
    year (int): Год выпуска
    nominal (int): Номинал монеты

    """
    def __init__(self, year:int, nominal:int) -> None:
        """Инициализирует объект класса Numizmat"""
        self.year = year
        self.nominal = nominal
        if not isinstance(year, int):  # проверяем, что год типа int
            raise TypeError("Год должен быть типа int")  # вызываем ошибку
        if not isinstance(nominal, int):  # проверяем, что номинал монеты типа int
            raise TypeError("Номинал должен быть типа int")  # вызываем ошибку
    def pozicia(self):
        """ Описывает монету
        >>> test1 = Numizmat(1951, 2)
        >>> test1.pozicia()
        'Монета номиналом 2 руб. выпущена в 1951 году.'
        """
        return f"Монета номиналом {self.nominal} руб. выпущена в {self.year} году."


class Calculyator:
    """
       Класс, складывающий два числа.

       Атрибуты:
       slag1 (int, float): первое слагаемое
       slag2 (int, float): второе слагаемое

       """

    def __init__(self, slag1: (int, float), slag2: (int, float)) -> None:
        """Инициализирует объект класса Calculyator"""
        self.slag1 = slag1
        self.slag2 = slag2
        if not isinstance(slag1, (int, float)) or not isinstance(slag2, (int, float)):
            raise TypeError("Слагаемые должны быть числового типа") #Вызываем ошибку

    def summa(self):
        """ Считает сумму
        >>> test2 = Calculyator(5.3, 2)
        >>> test2.summa()
        7.3
        """
        return self.slag1 + self.slag2
class Monopoly:
    """
    Класс, представляющий игру в монополию
    Атрибуты:
    player(str): игрок
    balance(int): счет игрока
    >>> test3 = Monopoly("Mаша", 4500)
    >>> test3.doxod(500)
    >>> test3.balance
    5000
    >>> test4 = Monopoly("Mаша", 4500)
    >>> test4.rasxod(4400)
    >>> test4.balance
    100
    """

    def __init__(self, player, balance=0):
        """
        Инициализирует игрока и его счет
        """
        if not isinstance(player, str):
            raise TypeError("Имя должно быть строкой.") #Вызываем ошибку
        if not isinstance(balance, int):
            raise TypeError("Счет должен быть числовым значением.") #Вызываем ошибку
        self.player = player
        self.balance = balance

    def doxod(self, renta):
        """
        Метод для получения игроком прибыли
        renta(int): сумма дохода
        вызывает исключение TypeError, если renta имеет неправильный тип данных.
        """
        if not isinstance(renta, int):

            raise TypeError("Сумма должна быть числовым значением.")
        self.balance += renta


    def rasxod(self, fine):
        """
        Метод для штрафования игрока
        fine(int): сумма штрафа
        вызывает исключение TypeError, если штраф имеет неправильный тип данных,
        или RuntimeError, если сумма штрафа больше, чем баланс игрока
        """
        if not isinstance(fine, int):

            raise TypeError("Сумма должна быть числовым значением.")
        if fine >= self.balance:
            raise RuntimeError("Игрок стал банкротом")
        self.balance -= fine


if __name__ == "__main__":
    # TODO работоспособность экземпляров класса проверить с помощью doctest
    doctest.testmod()
help(Numizmat)
help(Calculyator)
help(Monopoly)
