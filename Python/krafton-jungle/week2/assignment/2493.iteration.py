# 백준 2493 : 탑
# 역순 순회 -> O(N^2) -> 실패
import sys
input = sys.stdin.readline

N = int(input().strip())
stack = list(map(int, input().strip().split()))
results = []

while stack:
    send_num = stack.pop()
    found = False
    
    # 스택을 역순 순회
    for i in range(len(stack) - 1, -1, -1):
        if stack[i] > send_num:
            results.append(i+1)
            found = True
            break
    
    if not found:
        results.append(0)

sys.stdout.write('\n'.join(map(str, reversed(results))) + '\n')