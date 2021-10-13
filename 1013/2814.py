import sys
sys.stdin = open('2814_input.txt')

def dfs(v, cnt):
    global ans
    if ans < cnt:
        ans = cnt
    for w in range(1, V+1):
        if adj[v][w] == 1 and visited[w] == 0:
            visited[w] = 1
            dfs(w, cnt+1)
            visited[w] = 0

for tc in range(1, int(input())+1):
    V, E = map(int, input().split())
    adj = [[0] * (V+1) for _ in range(V+1)]
    visited = [0] * (V+1)
    for i in range(E):
        s, e = map(int, input().split())
        adj[s][e] = 1
        adj[e][s] = 1
    ans = 1
    for i in range(1, V+1):
        dfs(i, 0)
    print('#{} {}'.format(tc, ans))