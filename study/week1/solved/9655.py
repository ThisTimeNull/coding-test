# 백준 9655 : 돌 게임
import sys
input = sys.stdin.readline

N = int(input().strip())
result = 'SK' if N % 2 == 1 else 'CY'

print(result)