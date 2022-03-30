T = int(input())

def solve(k, n):
    floor_0 = [i for i in range(1, n+1)]

    for _ in range(k):
        for j in range(1, n):
            floor_0[j] += floor_0[j-1]
    return floor_0[-1]
    

for _ in range(1, T+1):
    k = int(input())
    n = int(input())

    print(solve(k,n))