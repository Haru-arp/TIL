import sys

sys.stdin = open('input.txt')

T = int(input())

for tc in range(1, T + 1):
    lst = input()
    sol = cnt = 0

    for i in range(len(lst)):
        if lst[i] == '(':
            cnt += 1
        else:
            if lst[i-1] == '(':
                cnt -= 1
                sol += cnt
            else:
                cnt -= 1
                sol += 1

    print(f'#{tc} {sol}')

