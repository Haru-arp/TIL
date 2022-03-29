import sys
sys.stdin = open('sample_input.txt')

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    dock = [list(map(int, input().split())) for _ in range(N)]
    #끝나는 시간을 기준으로 정렬
    dock.sort(key=lambda x: x[1])
    cnt = 1 #제일 빨리 끝나는 것을 선택하고 시작하기에 1로 초기화
    end = dock.pop(0) # 맨 처음께 끝나는것 맨 처음꺼 뽑자.

    # 다음 시작이 앞의 끝나는 시간 안에 있으면 삭제
    while dock:
        if dock[0][0] < end[1]:
            dock.pop(0)
        else:
            cnt += 1
            end = dock.pop(0) #갱신

    print(f'#{tc} {cnt}')