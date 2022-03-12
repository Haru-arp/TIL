import sys
sys.stdin = open('input.txt')

T = int(input())
for tc in range(1, T+1):
    lst = list(map(int, input().split()))
    sum_num = 0
    for i in lst:
        sum_num += i
    sum_avg = round(sum_num/10)

    print(f'#{tc} {sum_avg}')