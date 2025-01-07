#Специальные методы классов
class House:
    #Задание 4 в модуле
    houses_history = []

    def __new__(cls, *args):
        if args:
            cls.houses_history.append(args[0])
        return super().__new__(cls)

    def __init__(self, name, number_of_floors):
        self.name = name
        self.number_of_floors = number_of_floors

    def __del__(self):
        print(f"{self.name} снесён, но он останется в истории")

    #После этой строки идут функции и методы с предыдущих заданий

    def go_to(self, new_floor):
        if new_floor <= 0 or new_floor > self.number_of_floors:
            print('Такого этажа не существует')
        else:
            for i in range(new_floor):
                print(i + 1)

    # Задание 2 в модуле
    def __len__(self):
        return self.number_of_floors

    def __str__(self):
        return f"Название: {self.name}, количество этажей: {self.number_of_floors}"

    # Задание 3 в модуле
    def __eq__(self, other):
        return self.number_of_floors == other.number_of_floors

    def __lt__(self, other):
        return self.number_of_floors < other.number_of_floors

    def __le__(self, other):
        return self.number_of_floors <= other.number_of_floors

    def __gt__(self, other):
        return self.number_of_floors > other.number_of_floors

    def __ge__(self, other):
        return self.number_of_floors >= other.number_of_floors

    def __ne__(self, other):
        return self.number_of_floors != other.number_of_floors

    def __add__(self, value):
        return self.number_of_floors + value

    def __radd__(self, value):
        return self.__add__(value)

    def __iadd__(self, value):
        return self.__add__(value)


h1 = House('Школа №5', 5)
print(House.houses_history)
h2 = House('Гостиница "Дубрава"', 11)
print(House.houses_history)
h3 = House('ТЦ Мегагринн', 6)
print(House.houses_history)

del h1
del h3

print(House.houses_history)