import sys
sys.stdin = open('input.txt')

def insert_heap(data):
    heap.append(data)
    idx = len(heap) - 1
    while idx > 1 and heap[idx] < heap[idx//2]:
        heap[idx], heap[idx//2] = heap[idx//2], heap[idx]
        idx //= 2

def get_sum_heap():
    value = 0
    idx = N // 2
    while idx:
        value += heap[idx]
        idx //= 2
    return value

T = int(input())
for tc in range(1, T+1):

    answer = 0
    N = int(input())
    user_input = list(map(int, input().split()))
    heap = [0]
    for data in user_input:
        insert_heap(data)
    answer = get_sum_heap()

    print(f'#{tc} {answer}')