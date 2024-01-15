

def sum_of_max_subMatrix(n, m, matrix):
    upSum = [[0 for _ in range(m + 1)] for _ in range(n + 1)]

    for i in range(1, n + 1):
        for j in range(1, m + 1):
            upSum[i][j] = upSum[i - 1][j] + upSum[i][j - 1] - \
                upSum[i - 1][j - 1] + matrix[i - 1][j - 1]

    ans = matrix[0][0]
    for i in range(1, n + 1):
        for j in range(1, m + 1):
            for k in range(i, n + 1):
                for l in range(j, m + 1):
                    current_sum = upSum[k][l] - upSum[i - 1][l] - \
                        upSum[k][j - 1] + upSum[i - 1][j - 1]
                    ans = max(ans, current_sum)

    return ans


matrix = [[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12], [13, 14, 15, 16]]

n1, m1 = 1, 1
n2, m2 = 2, 2

result1 = sum_of_max_subMatrix(n1, m1, matrix)
result2 = sum_of_max_subMatrix(n2, m2, matrix)

print(f"Result 1: {result1}")
print(f"Result 2: {result2}")
