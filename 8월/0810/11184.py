import sys
sys.stdin = open('11172_input.txt')
T = int(input())
for tc in range(1, T+1):
    print('#{}'.format(tc))
    N = int(input())
    W = N//2 + 1
    arr = [[''] * W for _ in range(N)]
    stt = 65
    s = N//2
    for i in range(W - 1, -1, -1):
        for j in range(N): # 0 1 2 3 4
            if s <= j <= N-1-s:
                arr[j][i] = stt
                stt += 1
        s -= 1
    for i in range(len(arr)):
        for j in range(len(arr[i])):
            if arr[i][j] == '':
                print(arr[i][j], end=' ')
            elif arr[i][j] > 90:
                print(chr(arr[i][j]-25), end=' ')
            else:
                print(chr(arr[i][j]), end=' ')
        print()




