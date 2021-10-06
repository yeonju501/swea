T = int(input())
for tc in range(1, T+1):
    print('#{}'.format(tc))
    N = int(input())
    arr = []
    for i in range(N):
        new = []
        arr.append(new)
        for j in range(i+1):
            if 1 < i and 1 <= j < i:
                new.append(arr[i-1][j-1] + arr[i-1][j])
            else:
                new.append(1)
            print(arr[i][j], end=' ')
        print()
