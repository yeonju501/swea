import sys
sys.stdin = open('11172_input.txt')
T = int(input())
for tc in range(1, T+1):
    print('#{}'.format(tc))
    N = int(input())
    stt = 64 + N*N
    for i in range(N):
        for j in range(N):
            print(chr(stt - j*N), end=' ')
        stt -= 1
        print()
