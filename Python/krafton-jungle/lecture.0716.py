def nsum(n):
    sum = 0
    for i in range(1, n+1):
        sum += i
    return sum

# 부메랑처럼 돌아오는 재귀함수 : 실행 도중 멈췄을 때, 답을 알 수 없음
def nsum_recursive(n):
    if n == 0: 
        return 0
    return n + nsum_recursive(n - 1)

# 꼬리 재귀 : 실행 모델이 직선적(부메랑처럼 돌아오지 않음) : 매 재귀마다 답 total에 저장 -> 실행 도중 값을 알 수 
# 반복문과 유사한 실행 모델 흐름을 가짐
def nsum_tail_recursive(n, total):
    if n == 0:
        return total
    return nsum_tail_recursive(n - 1, total + n)

def exp(base, n):
    result = 1
    for i in range(n):
        result *= base
    return result

def exp_while(base, n):
    result = 1
    while n > 0:
        result *= base
        n -= 1
    return result

def exp_recursive(base, n):
    if n == 0:
        return 1
    return base * exp_recursive(base, n - 1)

def exp_tail_recursive(base, n, total):
    if n == 0:
        return total
    return exp_tail_recursive(base, n-1, total * base)

def fast_exp(base, n):
    if n == 0:
        return 1
    if n % 2 == 0:
        return fast_exp(base, n // 2) * fast_exp(base, n // 2)
    else:
        return base * fast_exp(base, n - 1)
    
def fast_exp_tail_recursive(base, n, total):
    if n == 0:
        return total
    if n % 2 == 0:
        return fast_exp_tail_recursive(base * base, n // 2, total)
    else:
        return fast_exp_tail_recursive(base, n - 1, total * base)
    
def fibonacci(n):
    if n == 0:
        return 0
    if n == 1:
        return 1
    return fibonacci(n - 1) + fibonacci(n - 2)