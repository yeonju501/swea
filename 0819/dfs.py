'''
7 8
1 2 1 3 2 4 2 5 4 6 5 6 6 7 3 7
'''
def dfs(v):
    # 방문체크
    visited[v] = 1
    print(v, end=' ')

    # 시작정점(v)의 인접한 모든 정점(w)에 대해서,
    # 방문 안 한 정점이면 재귀호출
    for w in range(1, V+1):
        # 인접하고 방문 안한 정점
        if adj[v][w] == 1 and visited[w] == 0:
            dfs(w)

# 정점수, 가선수
V, E = map(int, input().split())
# 인접행렬
adj = [[0] * (V+1) for _ in range(V+1)]
# 방문체크용
visited = [0] * (V+1)
# 간선들
edges = list(map(int, input().split()))
# 인정행렬에 저장하기
for i in range(E):
    s, e = edges[2*i], edges[2*i+1]
    adj[s][e] = 1
    adj[e][s] = 1

#인정행렬 확인용
for i in range(V+1):
    print("{} | {}".format(i, adj[i]))

dfs(1)