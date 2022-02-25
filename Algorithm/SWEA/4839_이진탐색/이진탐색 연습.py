import sys
sys.stdin = open('input.txt')


def binary_search(page, target):
    left = 1
    right = page
    cnt = 0
    while left <= right:
        middle = int((left + right) / 2)
        if middle == target:
            return cnt

        elif middle < target:
            left = middle
            cnt += 1
        elif middle > target:
            right = middle
            cnt += 1




T = int(input())

for tc in range(1, T+1):
    P, A, B = map(int, input().split())

    countA = binary_search(P, A)
    countB = binary_search(P, B)

    if countA == countB:
        result = 0
    elif countA > countB:
        result = 'B'
    elif countA <countB:
        result = 'A'


    print(f'{tc} {result}')


