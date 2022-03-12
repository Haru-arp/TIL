import sys
sys.stdin = open('input.txt')

T = int(input())

for tc in range(1, T+1):
    lst = list(map(int, input().split()))
    sum_num = 0
    for i in range(len(lst)):
        if lst[i] % 2 != 0:
            sum_num = sum_num + lst[i]
        else:
            continue
    print(f'#{tc} {sum_num}')