# 백준 1904 : 01타일
import sys
input = sys.stdin.readline

dp = [0] * 1000001
dp[1] = 1
dp[2] = 2
def solve(n):
    for i in range(3, n + 1):
        dp[i] = (dp[i - 1] + dp[i - 2]) % 15746
    
    return dp[n]

n = int(input().strip())
print(solve(n))