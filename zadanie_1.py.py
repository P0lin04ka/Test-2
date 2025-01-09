# TODO Написать 3 класса с документацией и аннотацией типов
import doctest

class Table:
    """
    Создание и подготовка к работе объекта "Стол"
    
    (Допустим что все измеряется в сантиметрах)
    
    :param height: Высота стола
    :param lenght: Ширина стола

    Примеры:
    >>> table = Table(200, 400)  # инициализация экземпляра класса
    """
    def __int__(self, height: float, lenght: float):
        if not isinstance(height, (int, float)):
            raise TypeError("Высота стола может принимать только int или float")
        if height <= 0:
            raise ValueError("Высота стола не может принимать значение меньше или равеное 0")
        self.height = height

        if not isinstance(lenght, (int, float)):
            raise TypeError("Ширина стола может принимать только int или float")
        if lenght <= 0:
            raise ValueError("Ширина стола не может принимать значение меньше или равеное 0")
        self.lenght = lenght

    def new_high(self, high: float) -> float:
        """
        Функция добовляет высоту стола на указанное значение

        :param high: Добавленная высота

        :raise ValueError: Если high отрицательное число, то выдает ошибку
        
        Примеры:
        >>> table = Table(200, 400) # инициализация экземпляра класса
        >>> table.new_high(50)
        """
        
        if not isinstance(high, (int, float)):
            raise TypeError("Добавленная высота может быть только int или float")
        if high < 0:
            raise ValueError("Добавленная высота не может быть меньше 0")
        
        ... 

    def paint(self, color: str)-> str:
        """
        Функция красит стол в заданый существующий цвет

        :param add_visota: Цвет в который перекрасится стол

        Если цвет написан с ошибкой, то стол не красится и выдается ошибка

        Примеры:
        >>> table = Table(200, 400)
        >>> table.paint("red")
        """
        if not isinstance(high, str):
            raise TypeError("Добавленная высота может быть только str")
        ...
        
class Wood:
    """
    Создание и подготовка к работе объекта "Дерево"

    :param height: Высота ствола
    :param color: Цвет листьев дерева

    Примеры:
    >>> wood = Wood(500, 250)  # инициализация экземпляра класса
    """
    def __int__(self, height: float, color: str):
        if not isinstance(height, (int, float)):
            raise TypeError("Высота дерева может быть только int или float")
        if height <= 0:
            raise ValueError("Высота дерева не может быть меньше или равен 0")
        self.height = height

        if not isinstance(color, str):
            raise TypeError("Цвет может быть только str")
        self.color = color

    def paint_protect(self) -> bool:
        """
        Функция которая проверяет нанесена ли на дерево защитная краска

        :return: Нанесена ли на дерево защитная краска
        
        Примеры:
        >>> wood = Wood(500, 250)
        >>> wood.paint_protect()
        """
        ...
        
    def create_birdhouse(self) -> bool:
        """
        Функция которая создает скворченик

        :return: Создался ли скворечник

        (True если да, False если нет)

        Примеры:
        >>> wood = Wood(500, 250)
        >>> wood.create_birdhouse()
        """
        ...

class Phone:
    """
    Создание и подготовка к работе объекта "Телефон"

    :param functions: Количество функций
    :param price: Обьем памяти в гб

    Примеры:
    >>> phone = Phone(100, 250)  # инициализация экземпляра класса
    """
    def __int__(self, functions: int, memory: float):
        if not isinstance(functions, int):
            raise TypeError("Количество функций должно быть целым числом")
        if functions < 0:
            raise ValueError("Количество функций не может быть отрицательным числом")
        self.functions = functions
        
        if not isinstance(memory, float):
            raise TypeError("Обем памяти должен быть целым числом")
        if memory < 0:
            raise ValueError("Обьем памяти не может быть отрицательным числом")
        self.memory = memory

    def add_cd_card(self, gb: int) -> int:
        """
        Функция добовляет карту памяти на определенное количество гб

        :param gb: Количество добавленных гб

        Примеры:
        >>> phone = Phone(100, 64)
        >>> phone.add_cd_card(32)
        """
        ...
        if not isinstance(gb, int):
            raise TypeError("Количество добавленных гб должно быть целым числом")
        if gb < 0:
            raise ValueError("Количество добавленных гб не может быть отрицательным числом")

    def new_update(self, func_update: int) -> int:
        """
        Функция добовляет функции телефону

        :param update: Количество новых функций

        Примеры:
        >>> phone = Phone(100, 64)
        >>> phone.update(20) 
        """
        ... 
        if not isinstance(func_update, int):
            raise TypeError("Количество новых функций должно быть целым числом")
        if func_update < 0:
            raise ValueError("Количество новых функций не может быть отрицательным числом")
        
if __name__ == "__main__":
    # TODO работоспособность экземпляров класса проверить с помощью doctest
    doctest.testmod()
