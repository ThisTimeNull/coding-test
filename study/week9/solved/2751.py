# 백준 2751 : 수 정렬하기 2
import sys

N = int(input().strip())

data = sorted([int(input().strip()) for _ in range(N)])
for i in range(N):
    print(data[i])