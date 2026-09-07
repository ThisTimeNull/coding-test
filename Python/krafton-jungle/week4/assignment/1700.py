# 백준 1700 : 멀티탭 스케줄링
import sys
input = sys.stdin.readline

N, K = map(int, input().strip().split())
arr = list(map(int, input().strip().split()))

multi_tap = set()
count = 0 # 멀티탭에서 플러그를 뽑는 횟수

for i in range(K):
    if arr[i] in multi_tap:
        continue
    
    if len(multi_tap) < N:
        multi_tap.add(arr[i])
    else:
        is_plug_found = False
        
        # 멀티탭이 꽉 찼을 때, 뽑아야 할 플러그 찾기
        for plug in multi_tap:
            if plug not in arr[i+1:]:
                multi_tap.remove(plug)
                multi_tap.add(arr[i])
                count += 1
                is_plug_found = True
                break        
        
        if not is_plug_found:
            for j in range(K-1, i, -1):
                if arr[j] in multi_tap:
                    multi_tap.remove(arr[j])
                    multi_tap.add(arr[i])
                    count += 1
                    break
            
# 결과 출력
print(count)