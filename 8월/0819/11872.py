import sys
sys.stdin = open('11872_input.txt')


def dfs(v, ns):
    # 방문체크
    visited[v] = 1
    ns.append(v)


    for w in range(1, V+1):
        # 인접하고 방문 안한 정점
        if adj[v][w] == 1 and visited[w] == 0:
            dfs(w, ns)


T = int(input())
for tc in range(1, T+1):

    V, E = map(int, input().split())

    adj = [[0] * (V+1) for _ in range(V+1)]

    visited = [0] * (V+1)


    edges = []
    for i in range(E):
        a, b = map(int, input().split())
        edges.extend([a, b])
        s, e = edges[2*i], edges[2*i+1]
        adj[s][e] = 1
    l, n = map(int, input().split())
    ns = []
    dfs(l, ns)
    if n in ns:
        print('#{} 1'.format(tc))
    else:
        print('#{} 0'.format(tc))