import sys
sys.stdin = open('11172_input.txt')
T = int(input())
for tc in range(1, T+1):
    print('#{}'.format(tc))
    N = int(input())
    stt = 65
    for i in range(N):
        for j in range(N):
            if j%2 == 0:
                if stt + j * N > 90:
                    print(stt + j * N - 25, end=' ')
                else:
                    print(stt + j * N, end=' ')
            else:
                if (stt + j * N + N - j) > 90:
                    print(stt + j * N + N - j - 25, end=' ')
                else:
                    print(stt + j*N + N - j, end=' ')
        stt += 1
        print()
