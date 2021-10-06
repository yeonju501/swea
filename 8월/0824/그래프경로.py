import sys
sys.stdin = open('11872_input.txt')


def dfs(v):
    global flag
    # 방문체크
    visited[v] = 1
    if v == G:
        flag = 1
        return
    # v의 인접정점중에 방문 안 한 w 정점을 재귀호출
    for w in range(V+1):
        if adj[v][w] == 1 and not visited[w]:
            dfs(w)


T = int(input())
for tc in range(1, T+1):
    flag = 0
    V, E = map(int, input().split())
    # 인정행렬
    adj = [[0] * (V+1) for _ in range(V+1)]
    # 방문처리
    visited = [0] * (V+1)
    for i in range(E):
        s, e = map(int, input().split()) # 시작노드, 끝노드
        adj[s][e] = 1
    # 출발노드, 끝노드
    S, G = map(int, input().split())
    dfs(S)
    print('#{} {}'.format(tc, visited[G]))
    print('#{} {}'.format(tc, flag))
