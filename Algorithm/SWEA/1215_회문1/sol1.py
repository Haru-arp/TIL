import sys

sys.stdin = open('input.txt')

T = 10

def is_palindrome(word):
    if len(word) <= 1:
        return True
    elif word[0] == word[-1]:
        return is_palindrome(word[1:-1])
    else:
        return False

for tc in range(1, T + 1):
    N = int(input())
    words = [list(input()) for _ in range(8)]
    cnt = 0 #답

    words_trans = list(zip(*words))

    for i in range(8):
        for j in range(8-N+1):
            if is_palindrome(words[i][j:j+N]):
                cnt += 1

    for i in range(8):
        for j in range(8-N+1):
            if is_palindrome(words_trans[i][j:j+N]):
                cnt += 1



    print(f'#{tc} {cnt}')

