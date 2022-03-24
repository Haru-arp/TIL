import sys
sys.stdin = open('input.txt')

T = int(input())
for tc in range(1, T+1):
    N = float(input())
    result = ''
    # 2의 -1승부터 2의 -13승까지 계산
    for power in range(-1, -14, -1):
        result += str(int(N // (2 ** power)))
        N %= (2 ** power)
        print(result)
        # N == 0이면 이진수로 변환이 완료된 것이다. -> 반복문 종료

        if N == 0:
            break
    # 반복문이 강제종료 되지 않았다는 것은 이진수 변환에 13자리 이상이 필요한 것이다. -> overflow
    else:
        result = 'overflow'

    print(f'#{tc} {result}')