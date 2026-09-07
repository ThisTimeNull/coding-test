import sys
input = sys.stdin.readline

def dfs(students, num, visited, finished, result):
    visited[num] = True  # 현재 노드 방문 표시
    next_num = students[num]  # 다음 노드로 이동
    
    if not visited[next_num]:  # 다음 노드가 아직 방문되지 않았다면
        return dfs(students, next_num, visited, finished, result)
    elif not finished[next_num]:  # 다음 노드가 방문되었지만 아직 완료되지 않았다면
        while next_num != num:  # 사이클이 끝날 때까지
            result.append(next_num) # 사이클에 포함된 노드 추가
            next_num = students[next_num]  # 다음 노드로 이동
        result.append(num)
    
    finished[num] = True  # 현재 노드 탐색 완료 표시
    
result = []
T = int(input().strip())
for _ in range(T):
    n = int(input().strip()) # 각 테스트 케이스의 학생 수
    arr = list(map(int, input().strip().split())) # 각 테스트 케이스마다의 학생들의 번호
    
    students = {}
    for i in range(n):
        students[i+1] = arr[i]

    visited = [False] * (n + 1)
    finished = [False] * (n + 1)
    path = []
    for i in range(1, n + 1):
        if not visited[i]:
            dfs(students, i, visited, finished, path)

    result.append(n - len(path))

sys.stdout.write('\n'.join(map(str, result)) + '\n')