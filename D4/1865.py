import sys
sys.stdin = open('1865_input.txt')
"""
def dfs(person, ans):
    global answer
    if answer >= ans:
        return
    if person == N:
        if answer < ans:
            answer = ans
        return
    for i in range(N):
        if not visited[i]:
            visited[i] = 1
            dfs(person+1, ans * work[person][i] / 100)
            visited[i] = 0
 
 
T = int(input())
for tc in range(1, T+1):
    N = int(input())
    work = [list(map(int, input().split())) for i in range(N)]
    visited = [0] * N
    answer = 0
    dfs(0, 1)
 
    print('#{} {:6f}'.format(tc, round(answer * 100, 6)))
"""
def perm(k, hap):
    global ans
    if hap <= ans:
        return
    if N == k:
        if ans < hap:
            ans = hap
        return
    else:
        for i in range(N):
            if not used[i]:
                used[i] = 1
                perm(k+1, hap*p[k][i]/100)
                used[i] = 0


for tc in range(1, int(input())+1):
    N = int(input())
    p = [list(map(int, input().split())) for _ in range(N)]
    ans = 0
    used = [0] * N
    perm(0, 1)
    print('#{} {:6f}'.format(tc, round(ans*100, 6)))

