# 백준 2098 : 외판원 순회
import sys
sys.setrecursionlimit(10**7)
input = sys.stdin.readline

N = int(input().strip())
W = [list(map(int, input().strip().split())) for _ in range(N)]

# dp[현재 도시][방문 상태] = 최소 비용
dp = [[-1] * N for _ in range(N)]

def tsp(current, visited):
    