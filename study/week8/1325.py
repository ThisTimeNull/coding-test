# 백준 1325 : 효율적인 해킹
import sys
from collections import deque

N, M = map(int, input().strip().split())

graph = [[] for _ in range()]