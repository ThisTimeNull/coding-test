# 백준 1904 : 01타일
import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

dp = [0] * 1000001
# 재귀함수 형태
def solve(n, dp):
    if n == 1:
        return 1
    if n == 2:
        return 2
    
    if dp[n] != 0:
        return dp[n]
    
    dp[n] = (solve(n - 1, dp) + solve(n - 2, dp)) % 15746
    return dp[n]

n = int(input().strip())
print(solve(n, dp))