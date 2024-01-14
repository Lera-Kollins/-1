# TODO Написать 3 класса с документацией и аннотацией типов
from typing import Union
import doctest


class House:
    def __init__(self, square: Union[int, float], floors: int, material: str):
        """
        Создание и подготовка к работе объекта "Дом"

        :param square: Площадь дома
        :param floors: Количество этажей
        :param material: Материал несущих конструкций

        Примеры:
        >>> house = House(80, 2, 'брус') #инициализация экземпляра класса
        """
        self.square = None
        self.init_square(square)
        self.floors = None
        self.init_floors(floors)
        self.material = None
        self.init_material(material)

    def init_square(self, square) -> None:
        if not isinstance(square, (int, float)):
            raise TypeError("Площадь дома должна быть типа int или float")
        if square < 0:
            raise ValueError("Площадь дома должна быть положительным числом")
        self.square = square

    def init_floors(self, floors) -> None:
        if not isinstance(floors, int):
            raise TypeError("Количество этажей дома должно быть типа int")
        if floors < 0:
            raise ValueError("Количество этажей дома должно быть положительным числом")
        self.floors = floors

    def init_material(self, material) -> None:
        if not isinstance(material, str):
            raise TypeError("Материал дома должен быть типа str")
        self.material = material

    def rooms_on_the_floor(self, floor_area: Union[int, float]) -> dict:
        """
        Функция которая считает количество возможных комнат на этаже

        :param floor_area: Площадь необходимого этажа
        :raise ValueError: Если площадь необходимого этажа превышает площадь дома, то вызываем ошибку

        :return: Словарь { 'Тип комнаты' : количество }

        Примеры:
        >>> house = House(80, 2, 'брус')
        >>> house.rooms_on_the_floor(36.3)
        """
        if not isinstance(floor_area, (int, float)):
            raise TypeError("Площадь этажа должна быть типа int или float")
        if floor_area < 0:
            raise ValueError("Площадь этажа должна быть положительным числом")
        ...

    def house_price(self, cost_per_square_meter: Union[int, float]) -> int:
        """
        Функция которая подсчитывает стоимость дома

        :param cost_per_square_meter: Стоимость одного квадратного метра (средняя на рынке)

        :return: Стоимость дома

        Примеры:
        >>> house = House(80, 2, 'брус')
        >>> house.house_price(42)
        """
        if not isinstance(cost_per_square_meter, (int, float)):
            raise TypeError("Стоимость одного квадратного метра должна быть типа int или float")
        if cost_per_square_meter < 0:
            raise ValueError("Стоимость одного квадратного метра должна быть положительным числом")
        ...


class ProteinBar:
    def __init__(self, weight_g: int, calories: int, name: str):
        """
        Создание и подготовка к работе объекта "Протеиновый батончик"

        :param weight_g: Масса нетто батончика в граммах
        :param calories: Калорийность батончика
        :param name: Наименования батончика

        Примеры:
        >>> protein_bar = ProteinBar(40, 180, 'Bombbar') #инициализация экземпляра класса
        """
        self.weight_g = None
        self.init_weight_g(weight_g)
        self.calories = None
        self.init_calories(calories)
        self.name = None
        self.init_name(name)

    def init_weight_g(self, weight_g) -> None:
        if not isinstance(weight_g, int):
            raise TypeError("Вес батончика должен быть типа int")
        if weight_g < 0:
            raise ValueError("Вес батончика должен быть положительным числом")
        self.weight_g = weight_g

    def init_calories(self, calories) -> None:
        if not isinstance(calories, int):
            raise TypeError("Калорийность батончика должна быть типа int")
        if calories < 0:
            raise ValueError("Калорийность батончика должна быть положительным числом")
        self.calories = calories

    def init_name(self, name) -> None:
        if not isinstance(name, str):
            raise TypeError("Название батончика должно быть типа str")
        self.name = name

    def percentage_of_daily_value(self, calorie_norm: int) -> int:
        """
        Функция которая считает процент калорийности батончика от дневного потребления

        :param calorie_norm: Дневная норма калорий

        :return: Процент от дневного потребления

        Примеры:
        >>> protein_bar = ProteinBar(40, 180, 'Bombbar')
        >>> protein_bar.percentage_of_daily_value(1500)
        """
        if not isinstance(calorie_norm, int):
            raise TypeError("Дневная норма калорий должна быть типа int")
        if calorie_norm < 0:
            raise ValueError("Дневная норма калорий должна быть положительным числом")
        ...

    def average_cost(self, city: str) -> int:
        """
        Функция которая считает среднюю стоимость батончика

        :param city: Город, в котором необходимо узнать стоимость

        :return: Средняя стоимость батончика

        Примеры:
        >>> protein_bar = ProteinBar(40, 180, 'Bombbar')
        >>> protein_bar.average_cost('Санкт-Петербург')
        """
        if not isinstance(city, str):
            raise TypeError("Название города должно быть типа str")
        ...


class BankDeposit:
    def __init__(self, deposit_amount: Union[int, float], term_month: int, banks_name: str):
        """
        Создание и подготовка к работе объекта "Банковский вклад"

        :param deposit_amount: Сумма вклада
        :param term_month: срок вклада в месяцах
        :param banks_name: Наименования банка

        Примеры:
        >>> bank_deposit = BankDeposit(7000, 12, 'Сбербанк') #инициализация экземпляра класса
        """
        self.deposit_amount = None
        self.init_deposit_amount(deposit_amount)
        self.term_month = None
        self.init_term_month(term_month)
        self.banks_name = None
        self.init_banks_name(banks_name)

    def init_deposit_amount(self, deposit_amount) -> None:
        if not isinstance(deposit_amount, (int, float)):
            raise TypeError("Сумма вклада должна быть типа int или float")
        if deposit_amount < 0:
            raise ValueError("Сумма вклада должна быть положительным числом")
        self.deposit_amount = deposit_amount

    def init_term_month(self, term_month) -> None:
        if not isinstance(term_month, int):
            raise TypeError("Срок вклада должен быть типа int")
        if term_month < 0:
            raise ValueError("Срок вклада должен быть положительным числом")
        self.term_month = term_month

    def init_banks_name(self, banks_name) -> None:
        if not isinstance(banks_name, str):
            raise TypeError("Название банка должно быть типа str")
        self.banks_name = banks_name

    def interest_rate(self) -> int or float:
        """
        Функция которая определяет процентную ставку в данном банке

        :return: Процентная ставка в данном банке

        Примеры:
        >>> bank_deposit = BankDeposit(7000, 12, 'Сбербанк')
        >>> bank_deposit.interest_rate()
        """
        ...

    def income(self) -> int or float:
        """
        Функция которая считает доход по вкладу

        :return: Доход по вкладу

        Примеры:
        >>> bank_deposit = BankDeposit(7000, 12, 'Сбербанк')
        >>> bank_deposit.income()
        """
        ...


if __name__ == "__main__":
    # TODO работоспособность экземпляров класса проверить с помощью doctest
    doctest.testmod()
    pass
