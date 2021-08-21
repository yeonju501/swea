import sys
sys.stdin = open('1974_input.txt')

T = int(input())
for tc in range(1, T+1):
    print('#{}'.format(tc), end=' ')
    arr = [list(map(int, input().split())) for _ in range(9)]
    i = j = s = 0
    ans = 0
    sdoku = [0]*10
    sdoku_idx = []
    while s < 8:
        if len(sdoku) == 9 or arr[i][j] in sdoku:
            if len(sdoku) == 9:
                sdoku_idx.append(s)
            s += 1
            i = (s // 3) * 3  # 0 1 2
            j = (s % 3) * 3  #
            sdoku = []
        sdoku.append(arr[i][j])
        j += 1
        if j % 3 == 0:
            j = (s % 3) * 3
            i += 1
    print(sdoku_idx)
    for i in range(9):
        for j in range(9):
            sdoku[arr[i][j]] += 1
            sdoku[arr[j][i]] += 1
        else:
            if arr[i][0] < 3
    print(ans)









