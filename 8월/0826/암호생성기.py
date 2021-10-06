import sys
sys.stdin = open('')
T = int(input())
for tc in range(1, T+1):
    no = int(input())
    q = list(map(int, input().split()))

    cnt = 0
    temp = 0
    while True:
        temp = q.pop(0)
        temp -= cnt % 5 + 1
        q.append(temp)
        cnt += 1
        if temp == 0:
            break

    print('#{} {}'.format(tc), end=' ')
    for i in range(len(q)):
        print(q[i], end=' ')
    print()