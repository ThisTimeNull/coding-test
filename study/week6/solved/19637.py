# 백준 19637 : IF문 좀 대신 써줘
import sys
import bisect

input = sys.stdin.readline

n, m = map(int, input().split())
titles = {}
for _ in range(n):
    title, limit = input().strip().split()
    limit = int(limit)

    if limit not in titles:
        titles[limit] = title

scores = [int(input().strip()) for _ in range(m)]

result = []
limits = sorted(titles.keys())
for score in scores:
    idx = bisect.bisect_left(limits, score)
    
    if idx == len(limits):
        idx -= 1

    result.append(titles[limits[idx]])
    
sys.stdout.write("\n".join(result))