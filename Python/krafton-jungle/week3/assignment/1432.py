# 백준 1432 : 그래프 수정
import sys
from collections import deque
input = sys.stdin.readline

N = int(input().strip())
in_degree = [0] * (N + 1) # 진입차수(인덱스 0은 더미)
graph = [[] for _ in range(N + 1)] # 인접리스트 기반(인덱스 0은 더미)
for i in range(N):
    line = list(map(int, input().strip()))
    
    for j in range(N):
        if line[j] == 1:
            graph[i+1].append(j+1)
            in_degree[j+1] += 1

def topology_sort_bfs(N, graph, in_degree):
    sorted_arr = []
    queue = deque([i for i in range(1, N+1) if in_degree[i] == 0]) # 진입차수 0인 노드로 초기화
    
    while queue:
        node = queue.popleft()
        
        sorted_arr.append(node) # 위상정렬 결과 배열에 노드 추가
        for next_node in graph[node]:
            in_degree[next_node] -= 1
            
            if in_degree[next_node] == 0:
                queue.append(next_node)
    
    return sorted_arr

# 결과 출력
result = topology_sort_bfs(N, graph, in_degree)
print(' '.join(map(str, result)) if result else -1) # 정렬된 결과가 있으면 요구사항에 맞춰 출력