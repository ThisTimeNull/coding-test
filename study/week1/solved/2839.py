# 백준 2839 : 설탕 배달
import sys
input = sys.stdin.readline

N = int(input().strip())
dp = [float('inf')] * (N + 1)
dp[0] = 0

for kg in [3, 5]:
    for j in range(kg, N + 1):
        if dp[j - kg] != float('inf'):
            dp[j] = min(dp[j], dp[j - kg] + 1)
        
print(dp[N] if dp[N] != float('inf') else -1)