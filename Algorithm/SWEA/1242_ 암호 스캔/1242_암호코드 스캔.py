import sys
sys.stdin = open('input.txt')



def Hamsu(in_str):
    code = list() # 10진 암호 코드 하나하나씩 저장할 배열( 8개 채우면 빈 배열로 리셋)
    idx = len(in_str) - 1
    # in_str의 뒤 -> 앞으로 역순으로 조사
    while idx >= 0:
        # 1을 만나면 그 때부터 암호 코드 추출 시작
        if in_str[idx] == '1':




# 2진수 코드 비율 - > 10진수
pattern = [
    (3, 2, 1, 1), (2, 2, 2, 1), (2, 1, 2, 2), (1, 4, 1, 1),
    (1, 1, 3, 2), (1, 2, 3, 1), (1, 1, 1, 4), (1, 3, 1, 2),
    (1, 2, 1, 3), (3, 1, 1, 2)
]
# 16진수 -> 2진수
hex_to_bin = {
    '0': '0000', '1': '0001', '2': '0010', '3': '0011',
    '4': '0100', '5': '0101', '6': '0110', '7': '0111',
    '8': '1000', '9': '1001', 'A': '1010', 'B': '1011',
    'C': '1100', 'D': '1101', 'E': '1110', 'F': '1111'
}


T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())
    in_arr = [input() for _ in range(N)]
    in_arr = list(set(in_arr)) # 중복 row 제거

    decimal_codes = list()
    for i in range(len(in_arr)):
        arr = in_arr[i]
        for j in range(M):
            if arr[j] != '0' or arr[len(arr)-i-1] != '0':
                # 16진 코드 -> 2진 코드 변환
                binary_code = ''
                for k in range(M):
                    binary_code += hex_to_bin[arr[k]]
                    # rstrip()= 인자로 전달된 문자를 오른쪽에서 제거
                binary_code = binary_code.rstrip('0')
                # 2진 코드 -> 10진수 코드 변환( 유효성 검사, 중복검사 포함)
                # 함수를 넣긴 해야겠는데 살려주세요 당근당근.... ㅠㅠ
                Hamsu(binary_code)
                break
    result = 0
    code_length = len(decimal_codes)
    for i in range(code_length):
        result += sum(decimal_codes[i])
    print(f'#{tc} {result}')

