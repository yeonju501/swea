#  A
# B D
#C E F
import sys
sys.stdin = open('11172_input.txt')
T = int(input())
for tc in range(1, T+1):
    print('#{}'.format(tc))
    N = int(input())
    arr = [[' ']*(N*2-1) for _ in range(N)]
    stt = 65
    s = N
    for i in range(N):
        for j in range(i, N):
            arr[j][s - j - 1] = stt
            stt += 1
        s += 2
    for a in arr:
        for i in a:
            if type(i) == int:
                if i > 90:
                    i -= 25
                print(chr(i), end='')
            else:
                print(i, end='')
        print()
