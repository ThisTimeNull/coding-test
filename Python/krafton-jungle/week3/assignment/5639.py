import sys
sys.setrecursionlimit(10**6)

arr = []
while True:
    try:
        x = int(sys.stdin.readline())
        arr.append(x)
    except:
        break

def post_order(start, end):
    if start > end:
        return
    root = arr[start]
    idx = start + 1
    while idx <= end and arr[idx] < root:
        idx += 1
    post_order(start + 1, idx - 1)
    post_order(idx, end)
    print(root)

post_order(0, len(arr) - 1)

# ------------------------------------------------------------------------

# 백준 5639 : 이진 검색 트리
import sys
sys.setrecursionlimit(10**6)

arr = []
while True:
    try:
        x = int(input())
        arr.append(x)
    except:
        break

def post_order(arr):
    # 원소가 비어있으면 종료
    if not arr:
        return
    
    root_value = arr[0]
    left_subtree = []
    right_subtree = []
    
    # 왼쪽 서브트리와 오른쪽 서브트리 분리
    for value in arr[1:]:
        if value < root_value:
            left_subtree.append(value)
        else:
            right_subtree.append(value)
    
    # 후위순회
    post_order(left_subtree) # 왼쪽 서브트리
    post_order(right_subtree) # 오른쪽 서브트리
    print(root_value)
    
post_order(arr)