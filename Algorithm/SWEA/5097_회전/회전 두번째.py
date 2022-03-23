import sys
sys.stdin = open('input.txt')

T = int(input())

for tc in range(1, T+1):
    n, m = map(int, input().split())
    que_lst = list(map(int, input().split()))

    for _ in range(m):
        que_lst.append(que_lst.pop(0))

    print(f'#{tc} {que_lst[0]}')