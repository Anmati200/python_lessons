from math import inf
def divide(first, second):
    result = 0
    if second == 0:
        return print("Результат деления: ", inf)
    else:
        result = first / second
        return print("Результат деления: ", result)