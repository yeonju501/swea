import sys
sys.stdin = open('1861_input.txt')


for tc in range(1, int(input())+1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]
    visited = [0] * (N**2+1)
    dx = [0, 0, 1, -1]
    dy = [1, -1, 0, 0]
    for i in range(N):
        for j in range(N):
            for d in range(4):
                ni = i + dx[d]
                nj = j + dy[d]
                if 0 <= ni < N and 0 <= nj < N and arr[ni][nj] == arr[i][j]+1:
                    visited[arr[i][j]] = 1
    cnt = 1
    t = 0
    max_cnt = 0
    for i in range(N**2, -1, -1):
        if visited[i]:
            cnt += 1
        else:
            if max_cnt <= cnt:
                t = i + 1
                max_cnt = cnt
            cnt = 1
    print(f'#{tc} {t} {max_cnt}')

