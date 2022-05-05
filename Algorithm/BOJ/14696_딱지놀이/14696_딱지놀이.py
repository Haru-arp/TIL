n = int(input())
for _ in range(n):
    a = [0] * 4
    b = [0] * 4
    data_a = list(map(int, input().split()))
    data_b = list(map(int, input().split()))
    for i in data_a[1:]:
        a[4-i] += 1
    for i in data_b[1:]:
        b[4-i] += 1
    if a > b:
        print("A")
    elif b > a:
        print("B")
    else:
        print("D")