def dfs(i, j):
    global cnt
    dx = [0, 0, 1, -1]
    dy = [1, -1, 0, 0]
    if arr[i][j] == 3: # 3을 만나면 리턴
        cnt += 1
        return
    elif arr[i][j] == 1: # 벽을 만나면 리턴
        return
    elif arr[i][j] == 4: # 함정을 만나면 리턴
        return
    else:
        visited[i][j] = 1
        for d in range(4): # 4방향 돌리기
            di = i + dx[d]
            dj = j + dy[d]
            if 0 <= di < N and 0 <= dj < N and not visited[di][dj]: # di, dj가 범위 안에 있고 방문하지 않았으면 함수 호출
                dfs(di, dj)

def find():
    for i in range(N):
        for j in range(N):
            if arr[i][j] == 2:
                return i, j

for tc in range(1, int(input())+1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]
    visited = [[0] * N for _ in range(N)]
    cnt = 0
    i, j = find()
    dfs(i, j)
    if cnt:
        print('#{} {}'.format(tc, 1))
    else:
        print('#{} {}'.format(tc, 0))


