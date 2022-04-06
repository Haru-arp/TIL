A, B = map(int, input().split()) # 1번 바구니에 사과, 오렌지
C, D = map(int, input().split()) # 2번 바구니에 사과, 오렌지

cnt = 0 # 과일을 옮기는 횟수 카운트

# 1번 바구니에는 사과만 2번 바구니에는 오렌지만 있어야 함.
print(min(A+D, B+C))