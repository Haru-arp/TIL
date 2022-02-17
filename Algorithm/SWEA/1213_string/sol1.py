import sys

sys.stdin = open('input.txt',  encoding='utf-8')

T = 10


for tc in range(1, T + 1):
    N = int(input())
    text = input()
    sentence = input()
    result = 0
    for i in range(len(sentence)):
        if sentence[i] == text[0]:
            if sentence[i: i+len(text)] == text:
                result += 1
    print(f'#{tc} {result} ')

