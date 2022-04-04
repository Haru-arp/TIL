P, M = map(int, input().split())
if P-M < 0 or (P-M)%2 != 0:
    print(-1)
else:
    p = (P+M)//2
    q = (P-p)

    print(max(p, q), min(p,q))