import sys
sys.stdin = open('11927_input.txt')


def in_order(n):
    global cnt
    if n * 2 <= N:
        in_order(n * 2)
    tree[n] = cnt
    cnt += 1
    if n * 2 + 1 <= N:
        in_order(n * 2 + 1)

T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    cnt = 1
    tree = [0] * (N + 1)
    in_order(1)
    print('#{} {} {}'.format(tc, tree[1], tree[N // 2]))

