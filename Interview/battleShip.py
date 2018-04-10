import sys

m = int(sys.stdin.readline().strip())
n = int(sys.stdin.readline().strip())
matrix = [[0] * n for _ in range(m)]
for i in range(m):
    matrix[i][:] = map(int, sys.stdin.readline().strip().split())

dp_row = [[0] * (n + 1) for _ in range(m + 1)]
dp_col = [[0] * (n + 1) for _ in range(m + 1)]
"""
分别计算各行/列连续出现1的个数
"""
for i in range(1, m + 1):
    for j in range(1, n + 1):
        if matrix[i - 1][j - 1] == 1:
            dp_row[i][j] = 1 + dp_row[i][j - 1]
            dp_col[i][j] = 1 + dp_col[i - 1][j]

for i in range(1, m + 1):
    for j in range(n - 1, 0, -1):
        if 0 < dp_row[i][j] < dp_row[i][j + 1]:
            dp_row[i][j] = dp_row[i][j + 1]

for j in range(1, n + 1):
    for i in range(m - 1, 0, -1):
        if 0 < dp_col[i][j] < dp_col[i + 1][j]:
            dp_col[i][j] = dp_col[i + 1][j]

max_val = 0
res = []

for i in range(1, m + 1):
    for j in range(1, n + 1):
        val = dp_row[i][j] + dp_col[i][j] - 1
        if max_val < val:
            max_val = val
            res = [(i - 1, j - 1)]
        elif max_val == val:
            res.append((i - 1, j - 1))

for v in res:
    print(str(v[0]) + ' ' + str(v[1]))
