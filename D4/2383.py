import sys
sys.stdin = open('2383_input.txt')


def check(dis, s):
    if s == 1:
        for i in range(1, stair1[2]):
            stair1_time[dis+i] += 1
    else:
        for i in range(1, stair2[2]):
            stair2_time[dis+i] += 1

for tc in range(1, int(input())+1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]
    flag = 0
    stair1 = []
    stair2 = []
    stair1_time = [0] * 100
    stair2_time = [0] * 100
    # 계단 저장
    for i in range(N):
        for j in range(N):
            if arr[i][j] >= 2:
                if not flag:
                    stair1 = [i, j, arr[i][j]]
                    flag = 1
                else:
                    stair2 = [i, j, arr[i][j]]

    # 어느 계단이 더 가까운지 계산
    for i in range(N):
        for j in range(N):
            if arr[i][j] == 1:
                if abs(i - stair1[0])+abs(j - stair1[1]) + stair1[2] <= abs(i - stair2[0]) + abs(j - stair2[1]) + stair2[2]:
                    s = 1
                    dis = abs(i - stair1[0])+abs(j - stair1[1])
                else:
                    s = 2
                    dis = abs(i - stair2[0]) + abs(j - stair2[1])
                # 계단에 시간 채우기
                check(dis, s)

    ans = 0
    for i in range(len(stair1_time)):
        if stair1_time[i]:
           if ans < i:
               ans = i
    for i in range(len(stair2_time)):
        if stair2_time[i]:
           if ans < i:
               ans = i
    print(f'#{tc}')
    print(stair1_time)
    print(stair2_time)
    print(ans+2)



    # 계단으로 간다
    # 가서 줄이 없으면 내려간다

