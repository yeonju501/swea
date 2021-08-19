
memo = [[0] * (10+1) for _ in range(10+1)]
for i in range(10):
    for j in range(i+1):
        if j == 0 or i == j:
            memo[i][j] = 1
        else:
            memo[i][j] = memo[i-1][j-1] + memo[i-1][j]

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    print('#{}'.format(tc))
    for i in range(N):
        for j in range(i+1):
            print('{}'.format(memo[i][j]), end=' ')
        print()