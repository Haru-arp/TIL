import sys
sys.stdin = open('sample_input.txt')


def find_set(x):
    """
        x를 포함하는 집합을 찾는 연산.
    """
    if x == parent[x]:
        return x
    else:
        return find_set(parent[x])

def union(x, y):
    """
        x와 y를 포함하는 두 집합을 통합하는 연산
    """
    parent[find_set(y)] = find_set(x)

T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())
    L = list(map(int, input().split()))
    # 출석 번호 인덱스까지 parent 리스트 만들어주기 (0번은 사용 안할거임)
    # 부모를 자기 자신으로 정의
    parent = [i for i in range(N+1)]

    # 두개씩 잘라서 한 쌍마다 union 연산
    for i in range(0, len(L), 2):
        union(L[i], L[i+1])

    result = set()
    for i in range(1, N+1):
        result.add(find_set(i))

    print(f'#{tc} {len(result)}')