# 백준 6416 : 트리인가?
import sys
input = sys.stdin.readline

test_case = 1
edges = []
while True:
    line = input().strip().split()
    if line[0] == '-1':
        break
    
    i = 0
    while i < len(line):
        a, b = line[i], line[i+1]

        if a == '0' and b =='0':
            # 이 시점에 간선 정보가 모두 들어온 거니까 이제 판별 로직 수행
            
            
            edges = [] # 간선 정보 초기화 
            test_case += 1 # 다음 테스트 케이스로
            break
        else:
            edges.append((int(a), int(b)))

        i += 2 # 다음 간선 정보 인덱스로 갱신