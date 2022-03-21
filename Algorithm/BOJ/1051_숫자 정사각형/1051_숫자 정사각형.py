N, M = map(int, input().split())
square = []
max_size = 1

for _ in range(N):
    square.append(list(map(int, input())))


def findSquare(row, col):
    size = 0
    for i in range(1, min(N, M) - min(row, col)):
        if row + i >= N or col + i >= M: continue
        if square[row][col] == square[row + i][col] == square[row][
                col + i] == square[row + i][col + i]:
            size = i + 1
    return size * size


for row in range(N - 1):
    for col in range(M - 1):
        size = findSquare(row, col)
        if max_size <= size:
            max_size = size

print(max_size)