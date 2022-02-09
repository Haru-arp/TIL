import sys

sys.stdin = open('input.txt')

T = int(input())


for tc in range(1, T + 1):
    N = int(input())
    TC = list(map(int,input().split())) #건물 높이
    max_value = 0

    for i in range(N):
        cnt = 0
        for j in range(i+1, N): #7 4 2 0 0 6 0 7 0
            if TC[i] > TC[j]:
                cnt += 1

        if cnt > max_value:
            max_value = cnt


    print(f'#{tc} {max_value} ')

