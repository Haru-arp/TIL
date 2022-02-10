import sys

sys.stdin = open('input.txt')

T = int(input())


for tc in range(1, T + 1):
    N = int(input())
    ai = list(map(int, input().split()))
    rlt = 0  #결과

#최대값 구하는 반복문
    max_ai = ai[0]
    for idx in ai:
        if max_ai < idx:
            max_ai = idx
#최소값 구하는 반복문
    min_ai = ai[0]
    for idx in ai:
        if min_ai > idx:
            min_ai = idx

    rlt = max_ai - min_ai

    print(f'#{tc} {rlt}')

