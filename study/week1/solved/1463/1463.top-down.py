# 백준 1463 : 1로 만들기
import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

N = int(input().strip())
# dp[i] = j : 정수 i에 대해 연산 최소 횟수
dp = [float('inf')] * (N + 1)

def solve(n):
    if n == 1:
        return 0
    
    if dp[n] != float('inf'):
        return dp[n]
    
    dp[n] = min(dp[n], solve(n-1) + 1)
    if n % 2 == 0:
        dp[n] = min(dp[n], solve(n // 2) + 1)
    if n % 3 == 0:
        dp[n] = min(dp[n], solve(n // 3) + 1)
    
    return dp[n]

print(solve(N))