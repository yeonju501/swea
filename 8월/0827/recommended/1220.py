import sys
sys.stdin = open('1220_input.txt')

for tc in range(1, 11):
    N = int(input())
    print('#{}'.format(tc), end=' ')
    arr = [list(map(int, input().split())) for _ in range(N)]
    # 1 : N => 위 / 2 : S => 아래
    # 1 은 아래로 2는 위로 그래서 1이 아래로 가다가 2
    cnt = 0
    for i in range(N):
        for j in range(N):
            if arr[j][i] == 1:
                flag = 1
            elif arr[j][i] == 2 and flag == 1:
                cnt += 1
                flag = 0
        else:
            flag = 0
    print(cnt)

