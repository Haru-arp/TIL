import sys

sys.stdin = open('input.txt')

T = int(input())


for tc in range(1, T + 1):
    a, b = input().split()
    len_a = len(a)
    len_b = len(b)
    i = 0
    key = 0
    while i < len_a:
        if a[i] == b[0]:
            if a[i:i+len_b] == b:
                key += 1
                i += len_b
            else:
                key += 1
                i += 1
        else:
            key += 1
            i += 1
    print(f'#{tc} {key}')

