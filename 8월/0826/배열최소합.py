import sys
sys.stdin = open('11883_input.txt')
def perm(n, k, cur_sum):
    global ans
    if ans < cur_sum:
        return
    if k == n:
        if ans > cur_sum:
            ans = cur_sum
    else:
        for i in range(k, n):
            order[k], order[i] = order[i], order[k]
            perm(n, k+1, cur_sum + arr[k][order[k]])
            order[k], order[i] = order[i], order[k]

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]
    order = list(range(N))
    ans = 987654321
    perm(N, 0, 0)
    print('#{} {}'.format(tc, ans))