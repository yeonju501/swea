import sys
sys.stdin = open('11775_input.txt')

def perm(n, k, hap):
    global ans
    if ans < hap:
        return
    if n == k:
        if ans > hap:
            ans = hap
    else:
        for i in range(n):
            if visit[i] == 0:
                visit[i] = 1
                perm(n, k+1, hap+arr[k][i])
                visit[i] = 0



for tc in range(1, int(input())+1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]
    visit = [0] * N
    ans = 5000
    perm(N, 0, 0)
    print('#{} {}'.format(tc, ans))