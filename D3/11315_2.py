import sys
sys.stdin = open('11315_input.txt')

def check():
    for i in range(N):
        for j in range(N):
            if arr[i][j] == 'o':
                for d in range(4):
                    cnt = 1
                    nx = i + dx[d]
                    ny = j + dy[d]
                    while 0 <= nx < N and 0 <= ny < N and arr[nx][ny] == 'o':
                        nx = nx + dx[d]
                        ny = ny + dy[d]
                        cnt += 1
                        if cnt == 5:
                            return 'YES'
                    else:
                        continue
    return 'NO'


T = int(input())
for tc in range(1, T+1):
    print('#{}'.format(tc), end=' ')
    N = int(input())
    arr = [list(input()) for _ in range(N)]
    dx = [1, 0, 1, 1]
    dy = [-1, 1, 1, 0]# 좌하, 우, 우하, 하
    print(check())
