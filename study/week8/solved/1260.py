# 백준 1260 : DFS와 BFS
import sys
from collections import deque
sys.setrecursionlimit(10**6)

input = sys.stdin.readline

N, M, V = map(int, input().strip().split())

graph = [[] for _ in range(N + 1)]
for _ in range(M):
    start_node, end_node = map(int, input().strip().split())
    graph[start_node].append(end_node)
    graph[end_node].append(start_node)
    
# 각 정점의 인접 리스트를 오름차순 정렬
for nodes in graph:
    nodes.sort()
    

def dfs(node, answer, visited):
    visited[node] = True
    
    for next_node in graph[node]:
        if visited[next_node] == False:
            answer.append(next_node)   
            dfs(next_node, answer, visited)
    
    return answer

def bfs(node, answer, visited):
    queue = deque([node])
    visited[node] = True
    
    while queue:
        pop_node = queue.popleft()
        
        for next_node in graph[pop_node]:
            if visited[next_node] == False:
                answer.append(next_node)
                visited[next_node] = True
                
                queue.append(next_node)
    
    return answer

dfs_result = dfs(V, [V], [False] * (N + 1))
bfs_result = bfs(V, [V], [False] * (N + 1))

print(' '.join(map(str, dfs_result)))
print(' '.join(map(str, bfs_result)))