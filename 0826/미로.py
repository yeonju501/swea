import sys
sys.stdin = open('11879_input.txt')

def find_start(arr):
    for x in range(N):
        for y in range(N):
            if arr[x][y] == 2:
                return x, y

def maze(x, y):
    global flag
    if arr[x][y] == 3:
        flag = 1
        return
    visited[x][y] = 1
    # 좌표에 인접하고 방문 안 한 좌표를 재귀호출
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]

        if nx < 0 or nx == N: continue # 인덱스 체크 (가장 먼저해야 함)
        if ny < 0 or ny == N: continue
        if visited[nx][ny] == 1: continue # 방문체크
        if arr[nx][ny] == 1: continue # 벽체크
        maze(nx, ny)

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

T = int(input())
for tc in range(1, T+1):
    flag = 0
    N = int(input())
    arr = [list(map(int, input())) for _ in range(N)]
    visited = [[0] * N for _ in range(N)]

    sx, sy = find_start(arr)
    maze(sx, sy)
    print('#{} {}'.format(tc, flag))
