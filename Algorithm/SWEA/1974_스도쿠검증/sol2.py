import sys

sys.stdin = open('input.txt')

T = int(input())
def garo():
    ans = 0
    for i in range(9):
        nums = list(range(1,10))
        cnt =0
        for j in range(9):
            if sudoku[i][j] in nums:
                nums.remove(sudoku[i][j])
                cnt += 1
            else:
                return False
        if cnt == 9:
            ans += 1
    if ans == 9:
        return True
    return False

def sero():
    ans = 0
    for i in range(9):
        nums = list(range(1, 10))
        cnt = 0
        for j in range(9):
            if sudoku[j][i] in nums:
                nums.remove(sudoku[j][i])
                cnt += 1
            else:
                return False
        if cnt == 9:
            ans += 1
    if ans == 9:
        return True
    return False

def byThree():
    ans = 0
    for i in range(0, 7, 3):
        for j in range(0, 7, 3):
            nums = list(range(1, 10))
            cnt = 0
            for di in range(3):
                for dj in range(3):
                    if sudoku[di+i][dj+j] in nums:
                        nums.remove(sudoku[di+i][dj+j])
                        cnt += 1
                    else:
                        return False
            if cnt == 9:
                ans += 1
    if ans == 9:
        return True
    return False



for tc in range(1, T + 1):
    sudoku = [list(map(int, input().split())) for _ in range(9)]

    print(f'#{tc}', end=' ')
    if garo() and sero() and byThree():
        print(1)
    else:
        print(0)


