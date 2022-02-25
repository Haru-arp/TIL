import sys
sys.stdin = open('input.txt')

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    ai = list(map(int, input()))

    cnt = [0] * 10

    for i in ai:
        cnt[i] += 1



    max_cnt = max(cnt)


    for j in range(len(cnt)):
        if max_cnt == cnt[j]:
            max_num = j


    print(f'#{tc} {max_num} {max_cnt}')
