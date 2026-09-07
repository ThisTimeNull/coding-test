# 백준 2407 : 조합
import sys
input = sys.stdin.readline

n, m = map(int, input().strip().split())
dp = [-1] * (n + 1)
dp[0] = 0
dp[1] = 1

# C(n,r) = n! / (r! × (n-r)!)
def factorial_dp(n):
    if n <= 1:
        return n
    
    if dp[n] != -1:
        return dp[n]
    
    dp[n] = factorial_dp(n-1) * n
    return dp[n]

result = factorial_dp(n) // (factorial_dp(m) * factorial_dp(n-m))
print(result)