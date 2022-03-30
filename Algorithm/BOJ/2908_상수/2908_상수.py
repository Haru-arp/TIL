A, B = input().split()
# 숫자를 거꾸로 읽어보자

A = A[::-1]
B = B[::-1]

if A > B:
    print(A)
else:
    print(B)
