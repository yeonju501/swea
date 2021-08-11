T = int(input())
for tc in range(1, T+1):
    N = int(input())
    snail = [[0]*N for _ in range(N)]
    # 방향 전환
    dx = [0, 1, 0, -1]
    dy = [1, 0, -1, 0]
    mode = 0
    
    #초기 좌표
    x = y = 0
    snail[x][y] = 1

    for num in range(2, N**2+1):

        x += dx[mode]
        y += dy[mode]
        
        # 배열에 숫자 채우기
        snail[x][y] = num
        
        # 인덱스가 범위 안에있고, 숫자가 아직 안써졌다면 같은 모드 유지
        if 0 <= x + dx[mode] < N and 0 <= y + dy[mode] < N and not snail[x+dx[mode]][y+dy[mode]]:
            continue
        # 아니라면 모드 변경
        if mode != 3:
            mode += 1
        else:
            mode = 0
    print(f'#{tc}')
    for i in snail:
        print(*i)


