import sys
sys.stdin = open('1979_input.txt')

T = int(input())
for tc in range(1, T+1):
    print('#{}'.format(tc), end=' ')
    n, k = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(n)]
    cnt = ans = 0
    for i in range(n):
        cnt = 0
        for j in range(n):
            if arr[i][j]:
                cnt += 1
            else:
                if cnt == k:
                    ans += 1
                cnt = 0
        if cnt == k:
            ans += 1

    for i in range(n):
        cnt = 0
        for j in range(n):
            if arr[j][i]:
                cnt += 1
            else:
                if cnt == k:
                    ans += 1
                cnt = 0
        if cnt == k:
            ans += 1
    print(ans)














