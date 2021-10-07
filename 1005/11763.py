import sys
sys.stdin = open('11763_input.txt')

def calc(n, k, hap):
    global ans
    hap += arr[order[N-1]][order[N]]
    if ans > hap:
        ans = hap

def perm(n, k, hap):
    if ans < hap:
        return
    if n == k:
        calc(n, k, hap)
    else:
        for i in range(n):
            if visited[i]: continue
            order[k] = i
            visited[i] = 1
            perm(n, k+1, hap + arr[order[k-1]][order[k]])
            visited[i] = 0


for tc in range(1, int(input())+1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]
    order = [0] * N + [0]
    order[0] = 0
    visited = [0] * N
    visited[0] = 1
    ans = 987654321
    perm(N, 1, 0)
    print(f'#{tc} {ans}')
