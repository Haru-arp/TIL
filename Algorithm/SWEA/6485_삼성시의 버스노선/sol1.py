import sys

sys.stdin = open('input.txt')

T = int(input())


for tc in range(1, T + 1):
    N = int(input()) #노선 개수
    count = [0] * 5001 # 리스트 범위를 1부터 하기위해서 5001개 만들었습니다.
    for n in range(N):
        A, B = map(int, input().split()) #A,B값을 받아오고
        for j in range(A, B+1): # A,B까지 범위에서
            count[j] += 1 #count 리스트에 범위 안에 1씩 더해서 카운트 해줬습니다.
    P = int(input()) #버스 정류장 개수
    bus_stop = [] #버스 정류장을 빈 리스트로 받고
    for _ in range(P): #5번 반복할건데
        C = int(input()) # 버스정류장 번호
        bus_stop.append(count[C]) #버스정류장 리스트에 버스 정류장 번호의 인덱스를 가진 값을 count 리스트에서 가져온다
    print(f'#{tc}', ' '.join(map(str, bus_stop)))

