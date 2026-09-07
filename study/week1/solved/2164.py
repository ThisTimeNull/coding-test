# 백준 2164 : 카드2
import sys
from collections import deque
input = sys.stdin.readline

N = int(input().strip())
queue = deque([i for i in range(1, N+1)])

while len(queue) >= 2:
    queue.popleft()
    queue.append(queue.popleft())
    
print(queue[-1])