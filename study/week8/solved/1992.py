# 백준 1992 : 쿼드트리
import sys

input = sys.stdin.readline
N = int(input().strip())
matrix = [list(map(int, list(input().strip()))) for _ in range(N)]
result = []

def quad_tree(x,y,size):
    # 비교의 기준이 되는 숫자값
    standard_num = matrix[x][y]
    
    # 탐색하며 숫자가 모두 동일한지 확인
    for i in range(x, x + size):
        for j in range(y, y + size):
            # 만약 숫자가 동일하지 않으면 4등분하고 줄어든 사이즈에서 다시 압축 진행
            if matrix[i][j] != standard_num:
                new_size = (size // 2)
                
                result.append('(')
                quad_tree(x, y, new_size)
                quad_tree(x, y + new_size, new_size)
                quad_tree(x + new_size, y, new_size)
                quad_tree(x + new_size, y + new_size, new_size)
                result.append(')')
                
                return
            
    # 숫자가 모두 일치하는 경우 : 압축
    result.append(str(standard_num))

# 함수 실행 및 결과 출력    
quad_tree(0,0,N)
sys.stdout.write(''.join(result))