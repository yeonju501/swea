import sys
sys.stdin = open('11885_input.txt')

def p_idx(s):
    global idx
    j = idx
    idx += 1
    return [j, int(s)]

T = int(input())
for tc in range(1, T+1):
    print('#{}'.format(tc), end=' ')
    N, M = map(int, input().split())
    idx = 1
    p = list(map(p_idx, input().split()))
    q = []
    ans = []
    while True:
        if len(ans) == M:
            break
        if len(q) < N:
            q.append(p.pop(0))
        else:
            a = q.pop(0)
            if a[1] // 2 == 0:
                ans.append(a)
                if p:
                    q.append(p.pop(0))
                else:
                    q.append([-1, -100])
            else:
                a[1] //= 2
                q.append(a)
    print(ans[-1][0])














