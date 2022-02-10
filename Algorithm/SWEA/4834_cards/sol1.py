import sys

sys.stdin = open('input.txt')

T = int(input())


for tc in range(1, T + 1):
    N = int(input())  # 카드의 장 수
    ai = list(map(int, input()))  # 따로 분리하기 위해 숫자를 문자열로.
    max_card = ai[0];

    #숫자중 최대값
    for m in ai:
        if m > max_card:
            max_card = m

    #리스트를 세기 위해서 0으로 초기화된 리스트 생성 길이는 최대 카드의 +1
    count_list = [0] * (max_card + 1)

    #반복: 카드 개수만큼
    for i in range(0, N):
        count_list[ai[i]] += 1
        max_count = 0
        temp_card = 0
        #카운트 리스트의 길이만큼 돌아가는데
        for j in range(0, len(count_list)):
            if count_list[j] >= max_count: #만약에 카운트 리스트 안의 인덱스가 max_count보다 크거나 같으면
                max_count = count_list[j] #가장 큰 수의 장 수가 되고
                temp_card = j  #가장 많은 카드의 숫자가 인덱스 값이 된다.

    print('#{} {} {}'.format(tc, temp_card, max_count))

