# 백준 1707 : 이분 그래프
import sys
from collections import deque
input = sys.stdin.readline

K = int(input().strip()) # 테스트 케이스 수
for _ in range(K):
	V, E = map(int, input().strip().split())
	
	group = [None] * (V + 1)
	graph = [[] for _ in range(V + 1)]
	for _ in range(E):
		u,v = map(int, input().strip().split())
		graph[u].append(v)
		graph[v].append(u)

	result = True
