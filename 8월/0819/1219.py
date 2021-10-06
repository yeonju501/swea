import sys
sys.stdin = open('1219_input.txt')

def dfs(v, ns):
    # 방문체크
    visited[v] = 1
    ns.append(v)


    for w in range(0, 100):
        # 인접하고 방문 안한 정점
        if adj[v][w] == 1 and visited[w] == 0:
            dfs(w, ns)


for tc in range(1, 11):

    V, E = map(int, input().split())

    adj = [[0] * 100 for _ in range(100)]

    visited = [0] * 100
    edges = list(map(int, input().split()))
    for i in range(E):
        s, e = edges[2*i], edges[2*i+1]
        adj[s][e] = 1
    ns = []
    dfs(0, ns)
    if 99 in ns:
        print('#{} 1'.format(tc))
    else:
        print('#{} 0'.format(tc))