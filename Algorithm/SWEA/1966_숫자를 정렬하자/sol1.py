import sys

sys.stdin = open('input.txt')

def Bubble_sort(arr):
    for i in range(len(arr)-1, 0, -1):
        for j in range(i):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]

T = int(input())

for tc in range(1, T + 1):

    print(f'#{tc}', end=' ')
    N = int(input())
    numbers = list(map(int, input().split()))

    for i in range(N):
        Bubble_sort(numbers)

    for i in numbers:
        print(i, end=' ')
    print()

