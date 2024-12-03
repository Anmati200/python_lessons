def password_for_numbers():

    number = int(input('Введите число, для которого нужно подобрать пароль: ' ))
    my_list = []
    result_string = ''

    #Добавление уникальных пар необходимых чисел в список
    for i in range(1, number):
        for j in range(1, number):
            if number % (i + j) == 0 and i != j:
                elem_of_pair = sorted([i, j])
                if not elem_of_pair in my_list:
                    my_list.append(elem_of_pair)

    #Обработка списка для вывода пароля единым числом
    for pair in my_list:
        for item in pair:
            result_string += str(item)

    print('Пароль для числа: ', result_string)

password_for_numbers()