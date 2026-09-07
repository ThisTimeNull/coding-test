# 백준 2110 : 공유기 설치
import sys
input = sys.stdin.readline

N,C = map(int, input().strip().split())
houses = [int(input().strip()) for _ in range(N)]
houses.sort()


def binary_search(start, end):
    result = 0 # 가장 인접한 두 공유기 사이의 최대 거리
    
    while start <= end:
        mid = (start + end) // 2 # 공유기 사이의 거리
        count = 1
        last_installed = houses[0]
        
        for i in range(1,N):
            if houses[i] - last_installed >= mid:
                count += 1
                last_installed = houses[i]
        
        if count >= C:
            result = mid
            start = mid + 1
        else:
            end = mid - 1
    
    return result

result = binary_search(1, houses[-1] - houses[0])
print(result)