import sys
sys.stdin = open('input.txt')

def workpower(result, person): #result: 확률 계산해가는 값, person: 깊이, i번째 사람
    global max_result
    global visited
    # 끝까지 계산하지 않고 도중에 안될거 같으면... 1미만을 곱하면 점점 작아지기 때문에 더 가지말고 돌아가자
    # N <= 16 이므로 최악 16!까지 가는 것을 가지치기하자
    if result <= max_result:
        return
    # 깊이 제일 끝일때
    if person == N: # 모든 직원이 각 자 일을 맡아 다 할때, 최종 결과랑 비교
        if max_result <= result:
            max_result = result
        return
    # 재귀파트 짜자
    for j in range(N): # 전체 순회
        if visited[j] == 0: # 방문을 안했으면
            visited[j] = 1 # 방문처리
            workpower(result*arr[person][j]*0.01, person+1) #재귀 DFS
            visited[j] = 0 # 제자리로


T = int(input())
for tc in range(1, T+1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]
    visited = [0] * N
    max_result = 0 # 비교할 최대 확률 ( 0 %가 가장 낮다)
    workpower(1,0)
    final_result = format(max_result*100, '.6f')
    print(f'#{tc} {final_result}')