# 백준 1946 : 신입 사원
import sys
input = sys.stdin.readline

T = int(input().strip())
for _ in range(T):
    N = int(input().strip())
    applicants = [tuple(map(int, input().strip().split())) for _ in range(N)]
    applicants.sort()
    
    count = 1
    min_rank = applicants[0][1]
    for i in range(1, N):
        if applicants[i][1] < min_rank:
            count += 1
            min_rank = applicants[i][1]
            
    print(count)