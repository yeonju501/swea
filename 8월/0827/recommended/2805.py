import sys
sys.stdin = open('2805_input.txt')

T = int(input())
for tc in range(1, T+1):
    print('#{}'.format(tc), end=' ')
    N = int(input())
    arr = [list(map(int, input())) for _ in range(N)]
    cnt = 0
    for i in range(N):
        if 2*i+1 <= N :
            for j in range(N//2-i, N//2+i+1):
                cnt += arr[i][j]
        else:
            for j in range(N//2-(N-1-i), N//2+(N-1-i)+1):
                cnt += arr[i][j]

    print(cnt)