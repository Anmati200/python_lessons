#Словари и множества

my_dict = {'Vitalii':27, 'Andrey':43, 'Victor':17, 'Anton':23 }
print(my_dict)

#Вывод значения по существующему ключу
print(my_dict['Andrey'])

#Вывод значения, если мы не знаем существует ли ключ
print(my_dict.get('Andrey')) # пример, если существует
print(my_dict.get('Natalya')) # пример, если не существует

my_dict.update({'Natalya': 22, 'Aleksey':24})
delete_name = my_dict.pop('Victor')
print(delete_name)
print(my_dict)

#Операции над множествами
my_set = {437, 'lesson', 3.14, 437, 'арбуз', 'арбуз', False}
print(my_set)

#Добавление новых элементов множества
my_set.add('new_elem')
my_set.add(5)

#удаление
my_set.discard('lesson')

print(my_set)




