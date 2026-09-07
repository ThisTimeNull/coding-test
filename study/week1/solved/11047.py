# 백준 11047 : 동전 0
import sys
input = sys.stdin.readline

N, K = map(int, input().strip().split())
coins = [int(input().strip()) for _ in range(N)]
coins.sort(reverse=True)

required_min_coin_count = 0
for coin in coins:
    required_min_coin_count += (K // coin)
    K %= coin

print(required_min_coin_count)