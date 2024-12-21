# Фунцкия для подсчета суммы всех чисел и длин всех строк
def calculate_structure_sum(*any_structure):
    sum_elem = 0

    for i in any_structure:
        if isinstance(i, (list, tuple)): #проверка на вложенные списки и кортежи
            sum_elem += calculate_structure_sum(*i)
        elif isinstance(i, dict): #проверка на вложенные словари
            for key, value in i.items():
                if isinstance(key, (list, tuple, dict)): #проверка на вложенные структуры внутри словаря
                    sum_elem += calculate_structure_sum(key)
                    sum_elem += calculate_structure_sum(value)
                elif isinstance(value, str):
                    sum_elem += len(value)
                else:
                    sum_elem += len(key) + value
        elif isinstance(i, str):
            sum_elem += len(i)
        else:
            sum_elem += i
    return sum_elem


data_structure = [
    [1,2,3],
    {'a': 4, 'b': 5},
    (6, {'cube': 7, 'drum': 8}),
    "Hello",
    ((), [{(2, 'Urban', ('Urban2', 35) ): ''}])
]

result = calculate_structure_sum(data_structure)
print(result)