def get_matrix(m, n, value):
    matrix = [[value for j in range(n)] for i in range(m)]
    return matrix

print(get_matrix(3, 2, 7))
