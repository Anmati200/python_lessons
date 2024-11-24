#Средний балл

#Вводный список
grades = [[5,3,3,5,4], [2,2,2,3], [4,5,5,2], [4,4,3], [5,5,5,4,5]]

#Вводное множество
students = {'Johnny', 'Bilbo', 'Steve', 'Khendrik', 'Aaron'}

first = (grades[0][0]+grades[0][1]+grades[0][2]+grades[0][3]+grades[0][4])/5
second = (grades[1][0]+grades[1][1]+grades[1][2]+grades[1][3])/4
third = (grades[2][0]+grades[2][1]+grades[2][2]+grades[2][3])/4
fourth = (grades[3][0]+grades[3][1]+grades[3][2])/3
fifth = (grades[4][0]+grades[4][1]+grades[4][2]+grades[4][3]+grades[4][4])/5

#Вывод для проверки правильности расчетов
print(first," ", second,' ', third,' ', fourth,' ', fifth)

#Конвертация множества в список, для обращения к элементам
students = list(students)

#Сортировка списка по алфавиту, для правильного соотнесения имен и оценок
students = sorted(students)
#Инициализация переменной типа 'словарь'
average_point = {}
average_point.update({students[0]:first, students[1]:second, students[2]:third, students[3]:fourth, students[4]:fifth})
print(average_point)