import sys
sys.stdin = open('11197_input.txt')
T = int(input())
for tc in range(1, T+1):
    print('#{}'.format(tc))
    N, M = map(int,input().split())
    if M == 1:
        for i in range(1, N+1):
            for j in range(i):
                print('*', end='')
            print()
    elif M == 2:
        for i in range(N):
            for j in range(N-i):
                print('*', end='')
            print()
    elif M == 3:
        for i in range(N):
            print(' '*(N-i-1), end='')
            print('*'*(i*2+1), end='')
            print()

