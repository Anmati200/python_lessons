#Распаковка позиционных параметров
#Пункт №1
def print_params(a = 9, b = 'текст', c = True):
    print(a,b,c)

print_params()
print_params(3)
print_params(4, 'тест')
print_params(5, 4, 6)
print_params(b = 25) # вызов работает
print_params(c = [1,2,3]) # вызов работает

#Пункт №2
values_list = [False, 27, 3.14]
values_dict = {'a': 45, 'b': 14.586, 'c': 'словарь'}
print_params(*values_list)
print_params(**values_dict)

#Пункт №3
value_list_2 = ['третье_задание', 100]
print_params(*value_list_2, 42)