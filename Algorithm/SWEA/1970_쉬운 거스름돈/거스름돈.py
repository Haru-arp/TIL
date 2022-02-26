import sys
sys.stdin = open('input.txt')
T = int(input())
for tc in range(1, T+1):
    n = int(input())
    coin_lst = [0] * 8
    coin_types = [50000, 10000, 5000, 1000, 500, 100, 50, 10]
    for i in range(8):
        if n // coin_types[i] != 0:
            coin_lst[i] = n//coin_types[i]
            n %= coin_types[i]

    print(f'#{tc}')
    print(*coin_lst)