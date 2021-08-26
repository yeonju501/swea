import sys
sys.stdin = open('11886_input.txt')

def bfs(q):
    dx = [0, -1, 0, 1] # 우 상 좌 하
    dy = [1, 0, -1, 0]
    while q:
        a = q.pop(0)
        visited[a[0]][a[1]] = a[2]
        for mode in range(4):
            if 0 <= a[0] + dx[mode] < N and 0 <= a[1] + dy[mode] < N:
                if arr[a[0] + dx[mode]][a[1] + dy[mode]] == '3' and not visited[a[0] + dx[mode]][a[1] + dy[mode]]:
                    return a[2]
                elif arr[a[0] + dx[mode]][a[1] + dy[mode]] == '0' and not visited[a[0]+dx[mode]][a[1]+dy[mode]]:
                    q.append([a[0]+dx[mode], a[1]+dy[mode], a[2]+1])
    return 0


T = int(input())
for tc in range(1, T+1):
    print('#{}'.format(tc), end=' ')
    N = int(input())
    arr = [list(input()) for _ in range(N)]
    q = []
    visited = [[0] * N for _ in range(N)]
    for i in range(N-1, -1, -1):
        for j in range(N-1, -1, -1):
            if arr[i][j] == '2':
                q.append([i, j, 0])
                break
    print(bfs(q))


