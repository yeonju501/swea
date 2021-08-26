import sys
sys.stdin = open('11889_input.txt')


def bfs(n, v):
    q = []
    q.append([v, 0])
    while q:
        a = q.pop(0)
        visited[a[0]] = 1
        if a[0] == G:
            return a[1]
        for w in range(1, n+1):  # 1 v
            if adj[a[0]][w] == 1 and not visited[w]:
                q.append([w, a[1]+1])
    return 0


T = int(input())
for tc in range(1, T+1):
    print('#{}'.format(tc), end=' ')
    V, E = map(int, input().split())
    edges = [list(map(int, input().split())) for i in range(E)]
    adj = [[0] * (V+1) for _ in range(V+1)]
    visited = [0] * (V+1)
    S, G = map(int, input().split())
    for i in range(E):
        adj[edges[i][0]][edges[i][1]] = 1
        adj[edges[i][1]][edges[i][0]] = 1
    print(bfs(V, S))