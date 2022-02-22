import sys

sys.stdin = open('input.txt')

T = int(input())


for tc in range(1, T + 1):
    n = int(input())
    print(f'#{tc}')
    pascal = []
    for i in range(n):
        arr = []
        for j in range(i + 1): #i+1이 아니라  i로 가져오면 i가 0일때 없게 되기 때문에  i + 1부터
            if j == 0 or i == j: #제일 첫번쨰 항이 1 또는 맨 마지막 항이면
                arr.append(1)  #1을  arr스택에 넣어주고
                print(1, end=' ') #1을 출력한다.
            else:
                arr.append(pascal[i - 1][j - 1] + pascal[i - 1][j]) #위에 값과 그 옆의 값을 더해줘서 스택에 append해주고
                print(pascal[i - 1][j - 1] + pascal[i - 1][j], end=' ') #값 출력
        pascal.append(arr)
        print()
