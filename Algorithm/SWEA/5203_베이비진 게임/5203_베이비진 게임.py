import sys
sys.stdin = open('sample_input.txt')

T = int(input())

#이겼는지 체크를 위한 함수
def check(player):
    # 10장을 돌면서 검사
    for j in range(10):
        #만약 같은 카드 3장을 가지고 있으면 승리
        if player[j] == 3:
            return True
    # 마지막 7,8,9까지만 검사
    for k in range(8):
        #연속된다면 이기니까 종료
        if player[k] and player[k+1] and player[k+2]:
            return True
    # 패배했으면
    return False


for tc in range(1, T+1):
    cards = list(map(int, input().split()))
    # 각각의 인덱스가 카드 번호가 되도록, 플레이어 초기값 생성
    player1 = [0] * 10
    player2 = [0] * 10
    # 처음 시작은 비김
    winner = 0

    #주어진 카드를 한 장씩 주자
    for i in range(len(cards)):
        #먼저 플레이어 1부터 받는다. (짝수로)
        if not i % 2:
            # 카드 번호에 해당하는 플레이어1의 인덱스에 카드 장수 늘려주기
            player1[cards[i]] += 1
            #승리 조건을 만족했다면
            if check(player1):
                # 승자! 후 종료
                winner = 1
                break

        else:
            # 플레이어2도 플레이어1과 같이 동일하게 진행
            player2[cards[i]] += 1
            if check(player2):
                winner = 2
                break

    print(f'#{tc} {winner}')