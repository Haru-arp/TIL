import sys
sys.stdin = open('sample_input (1).txt')

T = int(input())
di,dj = (1,-1,0,0),(0,0,-1,1)
for tc in range(1, T+1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]
    # [1] 좌표 * 2
    for i in range(len(arr)):
        arr[i][0] *= 2
        arr[i][1] *= 2
    ans = 0
    for _ in range(4002): #끝에서 끝 -2000 ~ 2000
        #[1] 좌표 이동
        for i in range(len(arr)):
            arr[i][0] += dj[arr[i][2]]
            arr[i][1] += di[arr[i][2]]

        #[2] 좌표 중복되면 삭제 후보
        ddel, v = set(), set()
        for i in range(len(arr)):
            cj, ci = arr[i][0], arr[i][1]
            if (cj,ci) in v:
                ddel.add((cj,ci))
            v.add((cj,ci))

        # [3] 삭제 리스트에 있으면 삭제
        for i in range(len(arr)-1, -1, -1):
            if (arr[i][0], arr[i][1]) in ddel:
                ans += arr[i][3]
                arr.pop(i)

        if len(arr) < 2:
            break
    print(f'#{tc} {ans}')
