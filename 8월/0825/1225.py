import sys
sys.stdin = open('1225_input.txt')


for tc in range(1, 11):
    T = input()
    print('#{}'.format(tc), end=' ')
    q = list(map(int, input().split()))
    j = 1
    while True:
        ans = q.pop(0) - j
        if ans <= 0:
            ans = 0
            q.append(ans)
            break
        q.append(ans)
        if j != 5:
            j += 1
        else:
            j = 1
    for i in range(8):
        print(q[i], end=' ')
    print()

