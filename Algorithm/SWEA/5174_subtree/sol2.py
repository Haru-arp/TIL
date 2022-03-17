import sys
sys.stdin = open('input.txt')


def preorder(node):
    global cnt
    if node:
        preorder(arr[node][0])
        preorder(arr[node][1])
        cnt += 1

T = int(input())
for tc in range(1, T+1):
    E, N = map(int, input().split())
    arr = [[0 for _ in range(2)] for _ in range(E+2)]
    lines = list(map(int, input().split()))

    for i in range(0, len(lines), 2):
        if arr[lines[i]][0]:
            arr[lines[i]][1] = lines[i+1]

        else:
            arr[lines[i]][0] = lines[i+1]
    cnt = 0
    preorder(N)

    print(f'#{tc} {cnt}')