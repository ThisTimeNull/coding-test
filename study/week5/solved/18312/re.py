import sys
input = sys.stdin.readline

N, K = map(int, input().split())
K = str(K)

result = 0
for hour in range(N + 1):
    for minute in range(60):
        for second in range(60):
            time_str = f"{hour:02d}{minute:02d}{second:02d}"
            
            if K in time_str:
                result += 1

print(result)