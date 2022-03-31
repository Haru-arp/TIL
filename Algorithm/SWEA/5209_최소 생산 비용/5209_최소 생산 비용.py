import sys
sys.stdin = open('sample_input.txt')

# 비용 계산 함수
# 인덱스와 합을 받을 예정
# idx값은 y 값이라고 생각하고 코딩하자.
def cost(idx, total):
    global result
    # 가지치기 : 만약 값이 이미 구한 값을 초과한다면 종료
    if total >= result:
        return
    # 만약 검사를 다 마쳤다면
    if idx == N:
        # total 값은 결과 (위에서 이미 가지치기 했음)
        result = total
        return
    # N 만큼 돌면서 x 축 검사
    for i in range(N):
        # 만약 x의 인덱스가 방문한 적 없다면?
        if not visited[i]:
            # 방문 처리
            visited[i] = 1
            cost(idx+1, total+arr[idx][i])
            visited[i] = 0

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]

    visited = [0 for _ in range(N)]
    result = 100 * N
    cost(0, 0)
    print(f'#{tc} {result}')