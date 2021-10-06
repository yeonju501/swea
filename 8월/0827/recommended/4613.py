import sys
sys.stdin = open('4613_input.txt')

T = int(input())
for tc in range(1, T+1):
    # 맨 윗 줄은 흰색
    # 다음줄이 파란색보다 흰색이 많으면 파란색
    # 그 다음 파란색
    # 맨마지막 줄이 파란색보다 빨간색이 많으면 빨간색
    # 맨 아래줄은 빨간색

    # 남은 색깔 빼기 해서 정하기?
    N, M = map(int, input().split())
    arr = [list(input()) for _ in range(N)]
    check = [0] * N
    n_white = []
    n_red = []
    n_blue = []
    for i in range(N):
        n_white.append(arr[i].count('W'))
        n_red.append(arr[i].count('R'))
        n_blue.append(arr[i].count('B'))

    # 첫줄과 끝줄 뺀 것
    ans = 2 * M - n_white[0] - n_red[-1]
    front = N // 2
    back = N//2 + 1
    c = 0
    s_w = sum(n_white[:front])
    s_b = sum(n_blue[:front])
    for i in range(1, front):
        if s_w >= s_b:
            ans += M - n_white[i]
            s_w -= n_white[i]
            s_b -= n_blue[i]
        else:
            ans += M - n_blue[i]
            s_w -= n_white[i]
            s_b -= n_blue[i]
            check[i] = 1
    s_b = sum(n_blue[front:])
    s_r = sum(n_red[front:])
    for i in range(front, N):
        if s_b >= s_r:
            ans += M - n_blue[i]
            s_b -= n_blue[i]
            s_w -= n_white[i]
            check[i] = 1
        else:
            ans += M - n_red[i]
            s_b -= n_blue[i]
            s_r -= n_red[i]
            check[i] = 2
    print(ans)
    if 1 not in check:
        if n_blue[front-1] >= n_blue[front]:
            ans += n_white[front-1] - n_blue[front-1]
        else:
            ans += n_red[front] - n_blue[front]
    print(ans)


