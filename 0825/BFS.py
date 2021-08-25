"""
7 8
1 2 1 3 2 4 2 5 4 6 5 6 6 7 3 7
"""
def bfs(v):
    q = []
    q.append(v) # 인큐하고
    print(v, end=' ')
    while q:
        v = q.pop(0)
        for w in range(1, V+1):
            if adj[v][w] == 1 and not visited[w]:
                q.append(w)
                visited[w] = visited[v] + 1
                print(w, end=' ') # enqueue할 때 할 일 하기
# 정점수, 간선수
V, E = map(int, input().split())

# 정점들
edges = list(map(int, input().split()))

# 인접행렬
adj = [[0] * (V+1) for _ in range(V+1)]
visited = [0] * (V+1)
for i in range(E):
    s, e = edges[2*i], edges[2*i+1]
    adj[s][e] = adj[e][s] = 1

bfs(1)
print()
print(max(visited)-1) # 출발 정점에서 가장 멀리 떨어져 있는 정점간의 간선의 수
print(visited.index(max(visited)))