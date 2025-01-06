#Специальные методы классов
class House:
    #Задание 1 в модуле
    def __init__(self, name, number_of_floors):
        self.name = name
        self.number_of_floors = number_of_floors

    def go_to(self, new_floor):
        if new_floor <= 0 or new_floor > self.number_of_floors:
            print('Такого этажа не существует')
        else:
            for i in range(new_floor):
                print(i + 1)

    #Задание 2 в модуле
    def __len__(self):
        return self.number_of_floors

    def __str__(self):
        return f"Название: {self.name}, количество этажей: {self.number_of_floors}"

    #Задание 3 в модуле
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
h2 = House('Гостиница "Дубрава"', 7)


#Вывод в консоль созданных объектов
print(h1)
print(h2)

h1 = h1 + 10 # __add__
print (h1)
h1 = 10 + h1 # __radd__
print (h1)
h2 += 10 # __iadd__
print(h2)

print(h1 == h2) # __eq__
print(h1 < h2) # __lt__
print(h1 <= h2) # __le__
print(h1 > h2) # __gt__
print(h1 >= h2) # __ge__
print(h1 != h2) # __ne__
