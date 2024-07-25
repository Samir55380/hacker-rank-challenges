# 3x3 2d array
d = [[11, 2, 4], [4, 5, 6], [10, 8, -12]]


def diagonalDifference(arr):
    # Write your code here
    primary_diagonal = 0
    secondary_diagonal = 0
    for i in range(len(arr)):
        primary_diagonal += arr[i][i]
        secondary_diagonal += arr[i][len(arr) - i - 1]
    return abs(primary_diagonal - secondary_diagonal)

print(diagonalDifference(d))  # 15