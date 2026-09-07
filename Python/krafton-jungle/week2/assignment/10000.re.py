# 백준 10000 : 원 영역
# 참고자료
# 1. https://devlibrary00108.tistory.com/449
# 2. https://nkdev.tistory.com/99
# 3. https://just-live.tistory.com/entry/%EB%B0%B1%EC%A4%80%ED%8C%8C%EC%9D%B4%EC%8D%AC-10000%EB%B2%88-%EC%9B%90-%EC%98%81%EC%97%AD-%ED%95%B5%EC%8B%AC-%EC%A0%95%EB%A6%AC
import sys
sys.setrecursionlimit(10000)  # 재귀 깊이 제한 해제
input = sys.stdin.readline

N = int(input().strip())
circles = []
for _ in range(N):
    x, r = map(int, input().strip().split())
    circles.append((x-r, x+r))
circles.sort(key=lambda x: (x[0], -x[1]))

count = 1 # 바깥영역 있으므로 1로 초기화
# 추가로 만들어지는 원의 영역 개수를 계산하는 함수
def recursive_solve(current_circle_idx, next_circle_idx):
    global count

    # 끝점이 동일한 경우
    if circles[current_circle_idx][1] == circles[next_circle_idx][1]:
        count += 1
        return
    
    # 끝점이 다른 경우 : 다음 끝점을 시작점으로 갖는 다른 원이 있는지 확인하고, 있으면 재귀호출
    # 선형탐색 방식은 시간초과
    target = circles[next_circle_idx][1]
    for idx in range(next_circle_idx + 1, N):
        if circles[idx][0] == target:
            recursive_solve(current_circle_idx, idx)
            break
    
    # 없으면 그대로 종료
    return

for i in range(N-1):
    # 왼쪽이 겹치면, 재귀로 오른쪽이 겹쳐지는 원이 나올때까지 재귀
    if circles[i][0] == circles[i+1][0]:
        recursive_solve(i,i+1)

print(N + count) 