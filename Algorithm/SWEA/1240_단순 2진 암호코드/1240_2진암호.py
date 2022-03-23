import sys
sys.stdin = open('input.txt')

#코드 패턴 딕셔너리 형태로 저장
my_pattern = {
    '0001101': 0,
    '0011001': 1,
    '0010011': 2,
    '0111101': 3,
    '0100011': 4,
    '0110001': 5,
    '0101111': 6,
    '0111011': 7,
    '0110111': 8,
    '0001011': 9,
}
T = int(input())
for tc in range(1, T+1):
    # n, m값을 공백을 기준으로 저장
    n, m = map(int, input().split())
    # 입력값 받아오기
    arr = [input() for _ in range(n)]
    # 암호를 받아 줄 빈 공간 변수 만들기
    my_code = ''

    for i in range(n):
        # 리스트를 돌면서 한 줄의 합이 0이면 그 줄은 전체 0인것이니 무시하고 계속 진행
        if sum(map(int, list(arr[i]))) == 0:
            continue
        else:
            # 암호문 코드의 줄은 i번쨰 줄이다.
            v_code = arr[i]
            # 맨 뒤에서 부터 보면서 1이 나오면 거기부터 56개가 암호이므로
            for j in range(m-1, -1, -1):
                if v_code[j] == '1':
                    # my_code 변수에 저장하고 break.
                    my_code = v_code[j-55:j+1]
                    break
            break
    # my_code_list 변수에 my_code 에서 7개씩 잘라서 my_pattern 안에 있는 암호와 비교할것이다.
    my_code_list = [my_pattern[my_code[i:i+7]] for i in range(0, 56, 7)]
    # 홀, 짝수 번째 인덱스 암호들 담을 변수 선언
    odd = 0
    even = 0
    for i in range(7):
        # 짝수면
        if i % 2:
            # 짝수 변수에 my_code_list[i]번째 값을 더해주며 담아주고
            even += my_code_list[i]
        # 홀수면
        else:
            # 홀수 변수에 my_code_list[i]번째 값을 더해주면서 담아준다.
            odd += my_code_list[i]
    # 정답을 찾을 answer 변수에 조건에 맞게 홀수번째 인덱스 * 3 + 짝수 인덱스 + 검증코드
    answer = odd * 3 + even + my_code_list[-1]
    # 만약 answer 안의 값이 10으로 나눴을 떄 맞아 떨어진다면 정답이므로 출력
    if answer % 10 == 0:
        print(f'#{tc} {sum(my_code_list)}')
    # 아니면 정답이 아니므로 0 출력
    else:
        print(f'#{tc} 0')
