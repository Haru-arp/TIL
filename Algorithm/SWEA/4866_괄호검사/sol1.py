import sys

sys.stdin = open('input.txt')

T = int(input())


for tc in range(1, T + 1):
    sentence = input()
    lst = []
    result = 1
    for s in sentence:
        if s == '(' or s == '{':
            lst.append(s)
        elif s == ')' or s == '}':
            if len(lst) == 0:
                result = 0
                break
            elif s == ')' and lst.pop() == '{':
                result = 0
                break
            elif s == '}' and lst.pop() == '(':
                result = 0
                break
    if len(lst):
        result = 0
    print(f'#{tc}  {result}')

