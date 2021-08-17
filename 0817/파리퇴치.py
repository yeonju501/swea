T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(N)]

    ans = 0
    for x in range(N-M+1):
        for y in range(N-M+1):
            sum_value = 0
            for i in range(M):
                for j in range(M):
                    sum += arr[x+i][y+j]
            if ans < sum_value:
                ans = sum_value
    print('#{} {}'.format(tc, ans))