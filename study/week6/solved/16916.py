# 백준 16916 : 부분 문자열
import sys

input = sys.stdin.readline
S = input().strip()
P = input().strip()

if P in S:
    print(1)
else:
    print(0)