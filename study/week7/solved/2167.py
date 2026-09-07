# 백준 2167 : 2차원 배열의 합
import sys
input = sys.stdin.readline

n, m = map(int, input().strip().split())
array = [list(map(int, input().strip().split())) for _ in range(n)]

pre_sum = [[0] * (m + 1) for _ in range(n + 1)]
for i in range(1, n + 1):
    for j in range(1, m + 1):
        pre_sum[i][j] = array[i-1][j-1] + pre_sum[i-1][j] + pre_sum[i][j-1] - pre_sum[i-1][j-1]

k = int(input().strip())
for _ in range(k):
    i, j, x, y = map(int, input().strip().split())

    result = pre_sum[x][y] - pre_sum[i-1][y] - pre_sum[x][j-1] + pre_sum[i-1][j-1]
    print(result)