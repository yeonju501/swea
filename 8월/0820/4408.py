import sys
sys.stdin = open('4408_input.txt')

T = int(input())
for tc in range(1, T+1):
    print('#{}'.format(tc), end=' ')
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]
    for i in range(len(arr)):
        arr[i].sort()
    for i in range(N):
        for j in range(2):
            arr[i][j] = arr[i][j] / 2

    a = [0] * N
    t = 1
    for i in range(N):
        for j in range(i+1, N):
            if arr[i][0] < arr[j][0] < arr[i][1] or arr[i][0] < arr[j][1] < arr[i][1]:
                if not a[j]:
                    t += 1
                    a[j] += 1
            elif arr[i][0] == arr[j][0] and arr[i][1] == arr[j][1]:
                if not a[j]:
                    t += 1
                    a[j] += 1
    print(t)