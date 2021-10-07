import sys
sys.stdin = open('11764_input.txt')

for tc in range(1, int(input())+1):
    N, M = map(int, input().split())
    w = list(map(int, input().split()))
    t = list(map(int, input().split()))
    w.sort(reverse=True)
    t.sort(reverse=True)
    i = 0
    j = 0
    ans = 0
    while i < N and j < M:
        if w[i] > t[j]:
            i += 1
        else:
            ans += w[i]
            i += 1
            j += 1
    print('#{} {}'.format(tc, ans))

