import sys
sys.stdin = open('led.txt')
T = int(input())
for tc in range(1, T+1):
    N = int(input())
    led = [0] * (N+1)
    want_led = [0] + list(map(int, input().split()))
    cnt = 0

    for i in range(N+1):
        if i == 0:
            continue

        if led[i] == want_led[i]:
            continue

        else:
            for j in range(i, N+1):
                if j % i == 0:
                    if led[j] == 0:
                        led[j] = 1
                    else:
                        led[j] = 0
            cnt += 1

        if led == want_led:
            print(f'#{tc} {cnt}')
            break