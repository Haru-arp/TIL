a = list(map(int, input().split()))
b = list(map(int, input().split()))

S = sum(a)
T = sum(b)

if S == T:
    print(S)
else:
    print(max(S, T))