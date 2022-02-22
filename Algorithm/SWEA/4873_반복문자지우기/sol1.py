import sys

sys.stdin = open('input.txt')

T = int(input())


for tc in range(1, T + 1):
    sentence = input()
    lst = []
    for s in sentence:
        if lst and s == lst[-1]:
            lst.pop()
        else:
            lst.append(s)

    print(f'#{tc} {len(lst)}')

