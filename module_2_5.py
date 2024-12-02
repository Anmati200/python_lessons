#Функции

def get_matrix(n, m, value):
    matrix = []
    for i in range(n):
        matrix_inner = []
        matrix.append(matrix_inner)
        for j in range(m):
            matrix_inner.append(value)
    return matrix

test1 = get_matrix(7,3,4)
test2 = get_matrix(4,4,104)
print(test1)
print(test2)
