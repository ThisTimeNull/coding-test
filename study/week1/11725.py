# 백준 11725 : 트리의 부모 찾기
import sys
from collections import deque
input = sys.stdin.readline

N = int(input().strip())

graph = [[] for _ in range(N+1)] # 인접리스트 방식 그래프
visited = [False] * (N+1)

def bfs(graph, visited):
    