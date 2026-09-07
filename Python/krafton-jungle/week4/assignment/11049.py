# 백준 11049 : 행렬 곱셈 순서
import sys
sys.setrecursionlimit(10**7)
input = sys.stdin.readline

N = int(input().strip())

matrix = []
for _ in range(N):
    r, c = map(int, input().strip().split(()))
    matrix.append((r, c))
    
# dp[i][j] = 최소 연산 횟수 : i번째 행렬 ~ j번째 행렬까지 곱할 때 최소 곱셈 연산 횟수
dp = [[-1] * N for _ in range(N)]
def solve(start_index, end_index):
    if start_index == end_index:
        return 0
    if dp[start_index][end_index] != -1:
        return dp[start_index][end_index]
    
    dp[start_index][end_index] = float('inf')
    for k in range(start_index, end_index):
        cost = (
            solve(start_index, k) +
            solve(k + 1, end_index) +
            matrix[start_index][0] * matrix[k][1] * matrix[end_index][1]
        )
        dp[start_index][end_index] = min(dp[start_index][end_index], cost)

    return dp[start_index][end_index]

print(solve(0, N - 1))