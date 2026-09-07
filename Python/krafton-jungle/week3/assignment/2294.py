# 백준 2294 : 동전 2
import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

N, K = map(int, input().strip().split())
min_count = float('inf') # 사용한 동전의 최소 개수 : 불가능한 경우 -1
nums = [int(input().strip()) for _ in range(N)] # 각 동전의 가치

def dfs(acc, nums, cnt):
    global min_count
    
    # 이미 K를 넘어선 경우는 종료
    if acc > K:
        return

    # 누적합이 K와 동일한 경우, 최소 동전 개수로 갱신 
    if acc == K:
        min_count = min(min_count, cnt)
        return
    
    for num in nums:
        dfs(acc + num, nums, cnt + 1)

# 결과
dfs(0, nums, 0)
print(min_count if min_count != float('inf') else -1)