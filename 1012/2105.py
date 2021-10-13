# 대각선 방향에 사각형을 그려야 한다 ->몰라
# 같은 숫자가 있어서는 안된다 -> 중복체크
# 갔던 길을 되돌아가는 것도 안된다 -> 방문체크

import sys
sys.stdin = open('2105_input.txt')


def dfs(i, j, x, y, dir, cnt):
    global ans
    dx = [1, 1, -1, -1]  # 우하, 좌하, 우상, 좌상
    dy = [1, -1, -1, 1]
    if dir == 4:
        if i == x and j == y:
            if cnt > ans:
                ans = cnt
        return
    if 0 <= i < N and 0 <= j < N and not visited[i][j] and not used[arr[i][j]]:
        used[arr[i][j]] = 1
        visited[i][j] = 1
        dfs(i + dx[dir], j + dy[dir], x, y, dir, cnt+1)
        dfs(i + dx[dir], j + dy[dir], x, y, dir+1, cnt+1)
        visited[i][j] = 0
        used[arr[i][j]] = 0

for tc in range(1, int(input())+1):
    N = int(input())
    arr = [list(map(int,input().split())) for _ in range(N)]
    used = [0] * (N*N+1)
    visited = [[0] * N for _ in range(N)]
    ans = 0
    for i in range(N):
        for j in range(N):
            dfs(i, j, i, j, 0, 0)
    if ans:
        print('#{} {}'.format(tc,ans))
    else:
        print('#{} {}'.format(tc, -1))
