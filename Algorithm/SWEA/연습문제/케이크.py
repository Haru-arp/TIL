import sys
sys.stdin = open('cake.txt')

def cut(array):
    sum_rc = 0
    for i in range(N):
        sum_rc += sum(array[i])
        if sum_rc * 2 == total:
            return True
    return False


T = int(input())

for tc in range(1, T+1):
    N = int(input())
    cake = [list(map(int, input().split())) for _ in range(N)]

    #케이크 딸기 총 개수
    total = 0
    for i in range(N):
        total += sum(cake[i])

    if cut(cake) and cut(list(zip(*cake))):
        print(f'#{tc} 1')
    else:
        print(f'#{tc} 0')