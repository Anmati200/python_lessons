#Рекурсия

def get_multiplied_digits(number):
    str_number = str(number)
    first = int(str_number[0])
    if not first: #проверка, если в конце числа стоит ноль
        first = 1
        return first
    if len(str_number) == 1:
        return first
    else:
        return first * get_multiplied_digits(int(str_number[1:]))

print(get_multiplied_digits(12345))
print(get_multiplied_digits(10200300400050000))