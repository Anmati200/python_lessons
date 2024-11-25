#Условная конструкция. Операторы if, elif, else
while True: #для удобства проверки работы
#Объявляем 3 переменные и присвоим значения, введенные с консоли
    first = input('Введите первое число: ')
    second = input('Введите второе число: ')
    third = input('Введите третье число: ')

    if first == second == third:
        print(3)
    elif first != second and second != third and first!=third:
        print(0)
    else:
        print(2)
