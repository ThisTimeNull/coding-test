# 백준 1343 : 폴리오미노
import sys
input = sys.stdin.readline

input_string = input().strip()
arr = input_string.split('.') # . 기준 분할 -> 빈 문자열 또는 값

for i in range(len(arr)):
    length_x = len(arr[i])
    
    # X가 홀수개면 -1 출력하고 반복문 탈출
    if length_x % 2 == 1:
        print(-1)
        exit()
        
    arr[i] = ('AAAA' * (length_x // 4)) + ('BB' * ((length_x % 4) // 2))
    
print('.'.join(arr))