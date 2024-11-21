#Неизменяемые и изменяемые объекты. Кортежи и списки

immutable_var = (10, 2.5, 'coffee', False)
print(immutable_var)

#immutable_var[0] = 100
#print(immutable_var)
### Данные строки кода не выполняются, так как мы
### не можем изменять данные в кортеже

mutable_list = [100500, 'tea', 3.547, True]
print(mutable_list) #Вывод списка до изменений

mutable_list[1] = 'BubbleTea'
mutable_list[3] = False
mutable_list.append('pineapple')
print(mutable_list) #Вывод списка после изменений