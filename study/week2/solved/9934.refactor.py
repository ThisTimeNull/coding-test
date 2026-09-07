# 백준 9934 : 완전 이진 트리(리팩토링)
import sys
input = sys.stdin.readline

K = int(input().strip())
buildings = list(map(int, input().strip().split()))

def preorder_recursive(buildings, depth, result):
    # 기저 조건
    if not buildings:
        return
    
    mid = (len(buildings) // 2)
    result[depth].append(buildings[mid])
    preorder_recursive(buildings[:mid], depth + 1, result)
    preorder_recursive(buildings[mid+1:], depth + 1, result)
    
result = [[] for _ in range(K)]
preorder_recursive(buildings, 0, result)
for level in result:
    print(' '.join(map(str, level)))