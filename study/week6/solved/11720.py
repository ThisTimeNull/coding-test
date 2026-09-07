# 백준 11720 : 숫자의 합
import sys
input = sys.stdin.readline

N = int(input().strip())
numbers = list(map(int, input().strip()))

print(sum(numbers))