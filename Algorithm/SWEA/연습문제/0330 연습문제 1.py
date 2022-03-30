import sys
sys.stdin = open('0330_1.txt')


def quickSorting(arr, start, end):  # 정렬할 배열, 배열의 시작 인덱스, 마지막 인덱스
    if start >= end:  # 재귀함수를 끝내주기 위한 base case를 지정
        return

    pivot = start  # 맨 왼쪽 값을 pivot
    left = start + 1  # arr[pivot] 보다 큰 값을 저장할 left 인덱스
    right = end  # arr[pivot]보다 작은 값을 저장할 right 인덱스

    while left <= right:  # left와 right가 엇갈리지 않을 때까지
        while left <= end and arr[left] <= arr[pivot]:
            left += 1

        while right > start and arr[right] >= arr[pivot]:
            right -= 1

        # while문을 빠져나오면 arr[left]와 arr[right]는 각각 arr[pivot]보다 큰 값, 작은 값을 갖는다.

        if left > right:  # left와 right가 엇갈린 경우
            arr[right], arr[pivot] = arr[pivot], arr[right]

        else:  # 엇갈리지 않은 경우
            arr[left], arr[right] = arr[right], arr[left]

    # 배열을 pivot을 기준으로 두 개로 분할 후, 분할 된 배열 모두 퀵정렬 실행
    quickSorting(arr, start, right - 1)
    quickSorting(arr, right + 1, end)



T = int(input())
for tc in range(1, T+1):
    number = list(map(int, input().split()))
    quickSorting(number, 0, len(number)-1)
    print(number)