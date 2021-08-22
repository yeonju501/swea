import sys
sys.stdin = open('1974_input.txt')


def width_check(arr, x):
    sdoku2 = []
    for j in range(9):
        if arr[x][j] in sdoku2:
            return 0
        sdoku2.append(arr[x][j])
    return 1


def height_check(arr, y):
    sdoku = []
    for j in range(9):
        if arr[j][y] in sdoku:
            return 0
        sdoku.append(arr[j][y])
    return 1

def square_check(arr, x, y):
    sdoku3 = []
    for i in range(x-3, x):
        for j in range(y-3, y):
            if arr[i][j] in sdoku3:
                return 0
            sdoku3.append(arr[i][j])
    for s in range(x-3, x):
        if width_check(arr, s):
            for l in range(y-3, y):
                if height_check(arr, l):
                    return 1
    else:
        return 0

T = int(input())
for tc in range(1, T+1):
    print('#{}'.format(tc), end=' ')
    a = [list(map(int, input().split())) for _ in range(9)]
    flag = 0
    for i in range(3, 10, 3):
        for j in range(3, 10, 3):
            if square_check(a, i, j):
                flag = 1
                break
    print(flag)











