import sys
sys.stdin = open('input.txt')

def quick_sort(left, right):
    if left >= right:
        return
    pivot = left
    i = left + 1
    j = right - 1
    while i <= j:
        while i <= j and a[pivot] >= a[i]:
            i += 1
        while i <= j and a[pivot] <= a[j]:
            j -= 1

        if i <= j:
            a[i], a[j] = a[j], a[i]
    a[pivot], a[j] = a[j], a[pivot]

    quick_sort(left, j)
    quick_sort(j+1, right)


T = int(input())
for tc in range(1, T+1):
    N = int(input())
    a = list(map(int, input().split()))

    quick_sort(0, len(a))

    print(f'#{tc} {a[N//2]}')