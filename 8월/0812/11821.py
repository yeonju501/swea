import sys
sys.stdin = open('11821_input.txt')
T = int(input())
for tc in range(1, T+1):
    print('#{}'.format(tc), end=' ')
    N = int(input())
    r = [list(map(int, input().split())) for _ in range(N)]
    red = []
    blue = []
    for i in range(len(r)):
        if r[i][4] == 1:
            for j in range(r[i][0], r[i][2]+1):
                for k in range(r[i][1], r[i][3]+1):
                    if (j, k) not in red:
                        red.append((j, k))
        elif r[i][4] == 2:
            for j in range(r[i][0], r[i][2]+1):
                for k in range(r[i][1], r[i][3]+1):
                    if (j, k) not in blue:
                        blue.append((j, k))
    purple = 0
    for i in range(len(red)):
        for j in range(len(blue)):
            if red[i] == blue[j]:
                purple += 1
    print(purple)



