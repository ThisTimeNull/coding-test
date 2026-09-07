# 백준 11053 : 가장 긴 증가하는 부분 수열
import sys
input = sys.stdin.readline

N = int(input().strip())
A = list(map(int, input().strip().split()))

dp = [1] * N

for i in range(N):
    for j in range(i):
        if A[i] > A[j]:
            dp[i] = max(dp[i], dp[j] + 1)
            
print(max(dp))