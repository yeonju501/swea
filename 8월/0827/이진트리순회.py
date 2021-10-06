"""
13
1 2 1 3 2 4 3 5 3 6 4 7 5 8 5 9 6 10 6 11 7 12 11 13
"""
def pre_order(node):
    global cnt
    if node != 0:
        print(node, end=' ')
        cnt += 1
        pre_order(tree[node][0])
        pre_order(tree[node][1])
# 정점수
V = int(input())
# 간선수
E = V - 1
tree = [[0] * 3 for _ in range(V+1)]
edges = list(map(int, input().split()))

for i in range(E):
    p = edges[2 * i]
    c = edges[2 * i + 1]
    if not [p][0]:
        tree[p][0] = c
    else:
        tree[p][1] = c

    tree[c][2] = p

cnt = 0
pre_order(1)
print(cnt)




