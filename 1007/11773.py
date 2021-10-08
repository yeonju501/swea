import sys
sys.stdin = open('11773_input.txt')


def dfs(n, k, e, c):
    global ans
    if ans <= c:
        return
    if n == k:
        if ans > c:
            ans = c
    else:
        dfs(n, k + 1, arr[k] - 1, c + 1)
        if e > 0:
            dfs(n, k+1, e-1, c)

for tc in range(1, int(input())+1):
    arr = list(map(int, input().split()))
    N = arr[0]
    ans = N
    dfs(N, 2, arr[1]-1, 0)
    print('#{} {}'.format(tc, ans))