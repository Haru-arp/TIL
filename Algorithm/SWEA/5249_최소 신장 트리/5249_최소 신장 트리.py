import sys
sys.stdin = open('sample_input.txt')

#부모가 누구인지 가져오는 함수
def get_parent(x):
    if parent[x] != x:
        parent[x] = get_parent(parent[x])
    return parent[x]
# 부모를 병합하는 함수
def union_parent(x, y):
    a = get_parent(x)
    b = get_parent(y)
    if a > b:
        parent[a] = b
    else:
        parent[b] = a

# 부모가 같은지 비교하는 ㅎ마수
def find(x, y):
    return get_parent(x) == get_parent(y)


T = int(input())
for tc in range(1, T+1):
    answer = 0
    V, E = map(int, input().split())
    parent = [i for i in range(V+1)]
    edge = [list(map(int, input().split())) for _ in range(E)]
    #가중치를 기준으로 정렬(내림차순)
    edge.sort(key=lambda x: -x[2])
    #간선이 빌 때까지 반복
    while edge:
        a, b, v = edge.pop()
        #부모가 다른 경우에만(사이클이 안 생기는 경우)
        if not find(a,b):
            #부모를 병합한다.
            union_parent(a, b)
            # 정답에 값을 더한다.
            answer += v
    print(f'#{tc} {answer}')