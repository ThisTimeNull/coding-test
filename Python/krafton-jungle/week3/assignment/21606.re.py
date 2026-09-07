# 백준 21606 : 아침 산책
import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

N = int(input().strip()) # 정점 개수
A = [0] + list(map(int, input().strip()))
count = 0 # 가능한 서로 다른 산책 경로의 수

graph = [[] for _ in range(N + 1)]
for _ in range(N-1):
    u,v = map(int, input().strip().split())
    graph[u].append(v)
    graph[v].append(u) # 무방향 그래프
    
    # 경우 1 : 실내-실내 쌍인 경우
    if A[u] == 1 and A[v] == 1:
        count += 2

# 경우 2 : 실외 노드가 포함된 경우
visited = [False] * (N + 1)
def dfs(node):
    indoor_count = 0 # 실외노드와 인접한 실내노드의 수
    
    visited[node] = True # 방문처리
    for neighbor in graph[node]:
        # 실내 노드의 경우
        if A[neighbor] == 1:
            indoor_count += 1
        elif not visited[neighbor] and A[neighbor] == 0:
            # 실외노드인데 아직 방문 안 했다면
            indoor_count += dfs(neighbor)
        
    return indoor_count

# 결과 출력
for i in range(1, N+1):
    if A[i] == 0 and not visited[i]:
        indoor_count = dfs(i)
        count += indoor_count * (indoor_count - 1)
print(count)