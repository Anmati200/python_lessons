class House:
    def __init__(self, name, number_of_floors):
        self.name = name
        self.number_of_floors = number_of_floors

    def go_to(self, new_floor):
        if new_floor <= 0 or new_floor > self.number_of_floors:
            print('Такого этажа не существует')
        else:
            for i in range(new_floor):
                print(i + 1)

h1 = House('ЖК Курский', 10)
h1.go_to(5)
h2 = House('Гостиница "Дубрава"', 7)
h2.go_to(8)
h3 = House('Школа 5', 5)
h3.go_to(-3)