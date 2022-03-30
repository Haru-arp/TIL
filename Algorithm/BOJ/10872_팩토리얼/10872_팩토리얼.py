N = int(input())

def fac(n):
    result = 1
    if n> 0:
        result = n * fac(n-1)
    return result

ans = fac(N)
print(ans)
