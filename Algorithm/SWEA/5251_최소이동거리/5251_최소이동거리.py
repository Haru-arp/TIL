import sys
sys.stdin = open('sample_input (1).txt')

def dijkstra(s):
    distance[s] = 0

    # 노드의 개수만큼 반복
    for _ in range(N+1):
        #현재 위치에서 가장 가까운 거리에 있는 노드 찾기
        min_idx = -1
        min_val = float('inf')
        for i in range(N+1):
            if not visited[i] and distance[i] < min_val:
                min_idx = i
                min_val = distance[i]
        visited[min_idx] = 1

        # 해당 노드로부터 인접한 노드들의 거리 살펴보기
        for i in range(N+1):
            if mat[min_idx][i] and not visited[i]: #연결되어있고 방문 안했다면
                if distance[min_idx] + mat[min_idx][i] < distance[i]:
                    distance[i] = distance[min_idx] + mat[min_idx][i]



T = int(input())
for tc in range(1, T+1):
    N, E = map(int, input().split())
    edges = [list(map(int, input().split())) for _ in range(E)]

    # 그래프 표현
    mat = [[0 for _ in range(N+1)] for _ in range(N+1)]
    for s, e, w in edges:
        mat[s][e] = w

    # 초기화
    distance = [float('inf') for _ in range(N+1)]
    visited = [0] * (N+1)

    # 다익스트라 시작
    start = 0
    dijkstra(start)

    print(f'#{tc} {distance[N]}')