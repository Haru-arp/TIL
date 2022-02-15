import sys

sys.stdin = open('input.txt')

def binary_search(page, target): #누가 더 빨리 찾는지 알아내는 함수
    left = 1
    right = page
    count = 0
    while left <= right:
        mid_value = int((left+right)/2)             #중간값 구하기
        if mid_value == target:                     #중간값이 목표 페이지랑 같다면?
            return count                            #바로 카운트를 출력하면 된다.
        elif mid_value < target:                    #중간값이 목표 페이지보다 작으면?
            left = mid_value                        #left를 중간값으로 할게..
            count += 1                              #카운트를 1 늘려줘...
        elif mid_value > target:                    #위의 반대.
            right = mid_value
            count += 1

T = int(input())


for tc in range(1, T + 1):
    page, A, B = map(int, input().split())
    countA = binary_search(page, A)
    countB = binary_search(page, B)

    if countA > countB:
        result = 'B'
    elif countA < countB:
        result = 'A'
    else:
        result = 0
    print(f'#{tc} {result} ')

