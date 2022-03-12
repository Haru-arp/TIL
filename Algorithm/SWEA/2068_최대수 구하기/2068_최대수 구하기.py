import sys
sys.stdin = open('input.txt')

T = int(input())
for tc in range(1, T+1):
    num_lst = list(map(int, input().split()))
    max_num = 0
    for i in num_lst:
        if i >= max_num:
            max_num = i

    print(f'#{tc} {max_num}')