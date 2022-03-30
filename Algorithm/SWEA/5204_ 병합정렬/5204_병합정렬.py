import sys
sys.stdin = open('input.txt')

def merge_sort(data):
    global cnt #왼쪽 마지막 원소가 오른쪽 마지막 원소보다 큰 경우 cnt += 1
    # 원소가 1개이면 그냥 그대로 return
    # 이유: 이미 정렬 되어있어서..?
    if len(data) <= 1:
        return data
    # 배열의 원소가 2개 이상이면 배열을 두개로 나눠서 각각 정렬된 배열을 return 받는다.
    mid = len(data)//2
    left = merge_sort(data[:mid])
    right = merge_sort(data[mid:])
    l_len = len(left)
    r_len = len(right)
    # idx : 원본 배열의 index
    # l-idx : 왼쪽 배열의 index,
    # r_idx : 오른쪽 배열의 index
    idx = l_idx = r_idx = 0
    # 정렬된 왼쪽 배열과 오른쪽 배열을
    # 첫 번째 index부터 마지막 index까지 비교하면서 작은 값부터 가져와보자.
    # 두 배열 중 하나라도 탐색이 끝나면 반복문 종료
    while l_idx < l_len and r_idx < r_len:
        if left[l_idx] <= right[r_idx]:
            data[idx] = left[l_idx]
            l_idx += 1
        else:
            data[idx] = right[r_idx]
            r_idx += 1
        idx += 1
    # 왼쪽 배열의 탐색이 끝났다면, ( 오른쪽 배열에 값이 남아 있으면)
    if l_idx == l_len:
        # 가져오지 않은 값들을 다 가져온다.
        for i in range(r_idx, r_len):
            data[idx] = right[i]
            idx += 1
    # 오른쪽 배열의 탐색이 끝났다면 ( 왼쪽 배열에 값이 남아 있으면)
    elif r_idx == r_len:
        # 왼쪽 배열의 마지막 원소가 오른쪽 배열의 마지막 원소보다 크기 때문에
        # 왼쪽 배열에 값이 남아있다. 즉 카운팅 해준다.
        cnt += 1
        # 가져오지 않은 값들을 다 가져온다.
        for i in range(l_idx, l_len):
            data[idx] = left[i]
            idx += 1
    # 병합 정렬된 배열을 리턴.
    # 마지막 return인 경우에는 최종적으로 정렬도니 배열을 리턴
    # 아닌 경우에는 left, right, 변수로 병합 정렬된 중간 결과문 리턴
    return data


T = int(input())
for tc in range(1, T+1):
    N = int(input())
    data = list(map(int, input().split()))
    cnt = 0
    data = merge_sort(data)

    print(f'#{tc} {data[N//2]} {cnt}')
