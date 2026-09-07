# 백준 2504 : 괄호의 값
import sys
input = sys.stdin.readline

galhos = list(input().strip()) # 괄호열
stack = []

result = 0
temp_result = 1
for i in range(len(galhos)):
    galho = galhos[i]
    
    if galho == '(':
        temp_result *= 2
        stack.append(galho)
    elif galho == '[':
        temp_result *= 3
        stack.append(galho)
    elif galho == ')':
        if (not stack) or stack[-1] != '(':
            result = 0
            break
        
        if galhos[i-1] == '(':
            result += temp_result
        
        stack.pop()
        temp_result //= 2
    elif galho == ']':
        if (not stack) or stack[-1] != '[':
            result = 0
            break
        
        if galhos[i-1] == '[':
            result += temp_result
        
        stack.pop()
        temp_result // 3
if stack:
    print(0)
else:
    print(result)