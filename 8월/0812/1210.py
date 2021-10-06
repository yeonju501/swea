import sys
sys.stdin = open('1210_input.txt')

for tc in range(1, 11):
    T = int(input())
    print('#{}'.format(T), end=' ')
    i = 0
    j = 0
    stt = 1
    visited = []
    ladder = [list(map(int, input().split())) for _ in range(100)]
    while 0 <= i <= 99 and 0 <= j <= 99:
        if i == 99 and ladder[i][j] == 1:
            for x in range(len(visited)):
                ladder[visited[x][0]][visited[x][1]] = 1
            stt += 1
            i = 0
            j = stt
        elif ladder[i][j] == 2:
            print(stt)
            break
        if ladder[i][j] == 1:
            ladder[i][j] = 9
            visited.append([i, j])
            if 0 <= j+1 <= 99 and ladder[i][j+1] == 1:
                j += 1
            elif 0 <= j-1 <= 99 and ladder[i][j-1] == 1:
                j -= 1
            elif 0 <= i+1 <= 99:
                i += 1
        elif 0 <= j+1 <= 99 and ladder[i][j] == 0:
            j += 1
            stt += 1



