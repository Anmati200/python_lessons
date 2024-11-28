#Цикл While

my_list = [42, 69, 322, 13, 0, 99, -5, 9, 8, 7, -6, 5]

count_of_number = 0
size_of_my_list = len(my_list)

while count_of_number < size_of_my_list:
    if my_list[count_of_number] > 0:
        print(my_list[count_of_number])
        count_of_number+=1
    elif my_list[count_of_number] == 0:
        count_of_number+=1
    else:
        break

