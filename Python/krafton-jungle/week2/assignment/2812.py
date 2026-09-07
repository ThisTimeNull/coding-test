# 백준 2812 : 크게 만들기
import sys
input = sys.stdin.readline

N,K = map(int, input().strip().split())
nums = list(map(int, input().strip()))
stack = [] # 결과를 만들 스택
count = 0 # 숫자 몇 개가 지워졌는지 카운트하는 변수

for num in nums:
    # 들어갈 갑보다 스택의 최상단 값들이 더 작은 경우엔 최대한 빼내보기
    while stack and count < K and stack[-1] < num:
        stack.pop()
        count += 1
    stack.append(num)

# 아직 K개를 다 못 지운 경우 -> 뒤쪽에서 남은만큼 잘라내기
if count < K:
    stack = stack[:-(K-count)]

print(''.join(map(str, stack)))