import sys
sys.stdin = open('11200_input.txt')
T = int(input())
for tc in range(1, T+1):
    print('#{}'.format(tc))
    N, M = map(int, input().split())
    if M == 1:
        for i in range(1, N+1):
            if i <= N//2 + 1:
                print('*'*i, end='')
            else:
                print('*'*(N-i+1), end='')
            print()
    if M == 2:
        for i in range(1, N+1):
            if i <= (N//2 + 1):
                print(' '*((N//2+1)-i), end='')
                print('*'*i, end='')
            else:
                print(' '*(i-(N//2+1)), end='')
                print('*'*(N-i+1), end='')
            print()
    if M == 3:
        for i in range(N):
            if i <= N//2:
                print(' '*i, end='')
                print('*'*(N-i*2), end='')
            else:
                print(' '*(N-i-1), end='')
                print('*'*((i//2)*2+1), end='')
            print()
    if M == 4:
        for i in range(N):
            if i <= N//2:
                print(' '*i, end='')
                print('*'*(N//2-i+1), end='')
            else:
                print(' '*(N//2), end='')
                print('*'*((i//2)+1), end='')
            print()

