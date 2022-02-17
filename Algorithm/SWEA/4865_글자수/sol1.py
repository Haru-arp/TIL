import sys

sys.stdin = open('input.txt')

T = int(input())


for tc in range(1, T + 1):
    str1 = input()
    str2 = input()
    sub_cnt, cnt = 0, 0

    for i in str1:
        for j in str2:
            if i == j:
                sub_cnt += 1
        if sub_cnt > cnt:
            cnt = sub_cnt
        sub_cnt = 0

    print(f'#{tc} {cnt}')

