import sys
sys.stdin = open('11825_input.txt')

def selection_sort(arr, N):
    for i in range(N-1):
        idx = i
        # 짝수일 때 최대값
        if i%2 == 0:
            
            for j in range(i+1, N):
                if arr[idx] < arr[j]:
                    idx = j
        else:
            for j in range(i+1, N):
                if arr[idx] > arr[j]:
                    idx = j

        arr[i], arr[idx] = arr[idx], arr[i]

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    arr = list(map(int, input().split()))
    selection_sort(arr, N)
    print('#{}'.format(tc), end=' ')
    for i in range(10):
        print(arr[i], end= ' ')
    print()