N = 10
T = int(input())
memo = [[0] * (N+1) for _ in range(N+1)]
for i in range(N):
    for j in range(i+1):
        if j == 0 or i == j:
            memo[i][j] = 1
        else:
            memo[i][j] = memo[i-1][j-1] + memo[i-1][j]

for tc in range(1, T+1):
    n = int(input())
    print('#{}'.format(tc))
    for i in range(n):
        for j in range(i+1):
            print(memo[i][j], end='')
        print()



