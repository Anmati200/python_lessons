#Цикл for

numbers = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15]
primes = []
not_primes = []

for i in numbers:
    if i == 1:
        continue
    is_prime = True #сброс флага на исходно принятое значение
    for j in numbers:
        if j == 1 or i == j: #Для исключения деления на один и на себя, иначе все числа будут "не простыми"
           continue
        elif i % j == 0:
            is_prime = False # отработка флага для последующей записи в список not_primes.
            break
    if is_prime:
        primes.append(i)
    else:
        not_primes.append(i)

print('Исходный список данных чисел: ', numbers)
print('Список простых чисел: ', primes)
print('Список чисел, не являющихся простыми: ', not_primes)
