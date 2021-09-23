import sys
sys.stdin = open('11926_input.txt')

def pre_order(node):
    global cnt
    if node != 0:
        cnt += 1
        pre_order(tree[node][0])
        pre_order(tree[node][1])

T = int(input())
for tc in range(1, T+1):
    E, N = map(int, input().split())
    tree = [[0] * 3 for _ in range(E+2)]
    edges = list(map(int, input().split()))

    # 왼쪽, 오른쪽, 부모
    for i in range(E):
        p = edges[i * 2]
        c = edges[i * 2 + 1]
        if not tree[p][0]:
            tree[p][0] = c
        else:
            tree[p][1] = c

    tree[c][2] = p
    cnt = 0
    pre_order(N)
    print('#{} {}'.format(tc, cnt))
