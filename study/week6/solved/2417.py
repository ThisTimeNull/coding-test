# 백준 2417 : 정수 제곱근
# https://www.acmicpc.net/problem/2417
# sqrt나 ceil(n ** 0.5)를 사용하면 부동소수점 오차로 인해 오답처리됨
import sys

input = sys.stdin.readline
n = int(input().strip())

left, right = 0, n
while left < right:
    mid = ((left + right) // 2)

    if (mid * mid) < n:
        left = mid + 1
    else:
        right = mid

print(right)