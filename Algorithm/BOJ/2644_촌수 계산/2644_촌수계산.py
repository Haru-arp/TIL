from collections import deque

def dfs(vertex):
    global result
    if result > 0: # a->b까지 도착했으면 result 값이 변한다. 결과가 나왔으니 모든 함수를 종료
        return 

    if vertex == b: # a->b까지 도착
        result = visit.count(1)-1 #촌수는 배열의 길이에서 -1 
        return
    
    for neighbor in adj[vertex]: #현재 노드와 인접한 노드 중에서
        if visit[neighbor] == 0: #방문하지 않은 노드가 있으면
            visit[neighbor] = 1 #방문
            dfs(neighbor) #노드를 들고 다시 dfs
            visit[neighbor] = 0 #원하는 값에 도달하지 못하고 나오면 방문 목록에서 제거
    return

n = int(input())
a, b = map(int, input().split())
m = int(input())

adj = [[] for _ in range(n+1)]
for _ in range(m):
    s, e = map(int, input().split())
    adj[s].append(e)
    adj[e].append(s)

result = -1 #촌수를 따질 수 없을 때는 -1이므로 기본값으로 -1
visit = [0] * (n+1) # visited 배열의 길이로 촌수 계산
visit[a] = 1 # ,a를 시작으로 두고 계산.
dfs(a) 
print(result)
