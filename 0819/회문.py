import sys
sys.stdin = open('11867_input.txt')

T = int(input())
for tc in range(1, T+1):
    print('#{}'.format(tc), end=' ')
    N, M = map(int, input().split())
    arr = [input() for _ in range(N)]
    for i in range(N):
        for j in range(N-M+1):
            # 검사 : len(M) // 2
            flag = 1
            for k in range(M // 2):
                if arr[i][j+k] != arr[i][j+M-1-k]:
                    flag = 0
                    break
            if flag: # 회문
                for k in range(M):
                    print('{}'.format(arr[i][j+k]), end='')
                print()
    for i in range(N):
        for j in range(N-M+1):
            # 검사 : len(M) // 2
            flag = 1
            for k in range(M // 2):
                if arr[j+k][i] != arr[j+M-1-k][i]:
                    flag = 0
                    break
            if flag: # 회문
                for k in range(M):
                    print('{}'.format(arr[i][j+k]), end='')
                print()
