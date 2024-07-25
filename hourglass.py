# 6x6 2d array
d: list[list[int]] = [[1, 1, 1, 0, 0, 0],
    [0, 1, 0, 0, 0, 0],
    [1, 1, 1, 0, 0, 0],
    [0, 0, 2, 4, 4, 0],
    [0, 0, 0, 2, 0, 0],
    [0, 0, 1, 2, 4, 0]]


def highest_hourglass_sum(d: list[list[int]]) -> int:
    array_of_sum_values = []
    for i in range(4):
        for j in range(4):
            sum_value = d[i][j] + d[i][j + 1] + d[i][j + 2] + d[i + 1][j + 1] + d[i + 2][j] + d[i + 2][j + 1] + d[i + 2][j + 2]
            array_of_sum_values.append(sum_value)
    return max(array_of_sum_values)

print(highest_hourglass_sum(d))