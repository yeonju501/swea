import sys
sys.stdin = open('4012_input.txt')


def synergy(a):
    n = 0
    for i in range(len(a)):
        for j in range(i+1, len(a)):
            n += arr[a[i]][a[j]] + arr[a[j]][a[i]]
    return n

def comb(n, k):
    global ans
    if n == N//2:
        A = []
        B = []
        for i in range(N):
            if used[i]:
                A.append(i)
            else:
                B.append(i)
        taste_A = synergy(A)
        taste_B = synergy(B)
        if ans > abs(taste_A-taste_B):
            ans = abs(taste_A-taste_B)
        return ans

    for i in range(k, N):
        if used[i] == 0:
            used[i] = 1
            comb(n+1, i+1)
            used[i] = 0


for tc in range(1, int(input())+1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]
    used = [0] * N
    ans = 987654321
    comb(0, 0)
    print('#{} {}'.format(tc, ans))