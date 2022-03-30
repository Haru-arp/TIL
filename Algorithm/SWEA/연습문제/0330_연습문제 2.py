def powerset(k, sum_num):
    global cnt
    cnt += 1
    if sum_num > 10:  # 가지치기
        return
    if k == n:  # 목표도달
        if sum_num == 10:
            for i in range(n):
                if visited[i]:
                    print(arr[i], end=" ")
            print()
        return

    else:
        visited[k] = 1
        powerset(k + 1, sum_num + arr[k])
        visited[k] = 0
        powerset(k + 1, sum_num)


arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
n = len(arr)
cnt = 0
visited = [0] * n
powerset(0, 0)
