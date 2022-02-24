import sys

sys.stdin = open('input.txt')

T = 10

for tc in range(1, T + 1):
    n = int(input())
    buildings = list(map(int, input().split()))
    cnt = 0 #조망권 확보된 세대 수

    for i in range(2, n-2):


    print(f'#{tc} ')

