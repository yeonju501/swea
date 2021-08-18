T = int(input())
for tc in range(1, T+1):
    print('#{}'.format(tc))
    N = int(input())
    arr = []
    for i in range(1, N+1):
        arr.append([1]*i)
    for i in range(N):
        for j in range(i):
            if 1 < i < N and 1 <= j < N:
                arr[i][j] = arr[i-1][j-1] + arr[i-1][j]
    for i in range(N):
        for j in range(i+1):
            print(arr[i][j], end=' ')
        print()