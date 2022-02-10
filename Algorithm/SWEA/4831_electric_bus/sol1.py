import sys

sys.stdin = open('input.txt')

T = int(input())


for tc in range(1, T + 1):
    #K=최대 이동 가능 수
    #N :종점
    #M : 충전기 정류장 수
    K, N, M = map(int, input().split())

    #charge: 충전기의 위치치
    charge = list(map(int, input().split()))+[N+K, N+K] #N+K리스트를 2개 추가해 준 이유는
                                                        #반복문 돌 떄 마지막 값이 범위를 벗어나기 때문에
    #현재 위치
    here = 0
    #정류장 위치
    i = 0
    #충전 할 때마다 +1
    cnt = 0
    while here + K < N:  #현재 위치에서 최대로 이동했는데 종점보다 적을 때 동안
        if here+K >= charge[i+2]:
            here = charge[i+2] #현재 위치가 그 충전소 위치가 된다.
            cnt += 1 #충전을 한번 해준다
            i += 3 #정류장 위치를 3만큼 더해준다.
            continue

        elif here+K >= charge[i+1]: #또한 만약에 현재 위치에서 최대 이동가능한 만큼 이동한게 충전소에서 +1크기보다 크거나 같으면
            here = charge[i+1]
            cnt += 1
            i += 2
            continue
        elif here+K < charge[i]:
            cnt = 0 #충전 불가.
            break
        else:
            here = charge[i] #나머지 경우는 현재위치와 충전소 위치를 같게 해주고
            cnt += 1
            i += 1

    print(f'#{tc} {cnt} ')

