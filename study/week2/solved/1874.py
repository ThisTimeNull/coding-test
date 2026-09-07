# 백준 1874 : 스택 수열
import sys
input = sys.stdin.readline

N = int(input().strip())

result = [] # 결과 출력용
stack = []
current_num = 1
is_possible = True
for _ in range(N):
    target_num = int(input().strip())
    
    while current_num <= target_num:
        stack.append(current_num)
        result.append('+')
        current_num += 1

    if stack and stack[-1] == target_num:
        stack.pop()
        result.append('-')
    else:
        is_possible = False
        break

if is_possible:
    sys.stdout.write('\n'.join(map(str, result)) + '\n')
else:
    print('NO')