# 백준 17626 : Four Squares
import sys
input = sys.stdin.readline

n = int(input().strip())

if n == 1:
    print(1)
else:
    dp = [0] * (n + 1)
    dp[1] = 1
    
    i = 1
    while i <= n:
        dp[i^2] += 1
        i += 1