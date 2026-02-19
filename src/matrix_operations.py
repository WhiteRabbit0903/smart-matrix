def multiply_matrix(a, b):
    result = []
    for i in range(len(a)):
        row = []
        for j in range(len(b[0])):
            sum_value = 0
            for k in range(len(b)):
                sum_value += a[i][k] * b[k][j]
            row.append(sum_value)
        result.append(row)
    return result
