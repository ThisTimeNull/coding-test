# 백준 1541 : 잃어버린 괄호
import sys
input = sys.stdin.readline

expression = input().strip()
parts = expression.split('-')

total = 0
for i, part in enumerate(parts):
    if i == 0:
        total += sum(map(int, part.split('+')))
    else:
        total -= sum(map(int, part.split('+')))

# 결과 출력
print(total)