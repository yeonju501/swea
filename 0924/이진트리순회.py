"""
13
1 2 1 3 2 4 3 5 3 6 4 7 5 8 5 9 6 10 6 11 7 12 11 13
"""
def pre_order(node):
    global cnt
    if node != 0 :
        print(node, end=' ')  # 할일
        cnt += 1
        pre_order(tree[node][0])
        pre_order(tree[node][1])


#정점수
V = int(input())
#간선의 수
E = V - 1
# tree
tree = [[0] * 3 for _ in range(V+1)]
edges = list(map(int, input().split()))

# 왼쪽, 오른쪽, 부모
for i in range(E):
    p = edges[i * 2]
    c = edges[i * 2 + 1]
    if not tree[p][0]: # 왼쪽자식이 없으면
        tree[p][0] = c
    else:               # 왼쪽자식이 있으면
        tree[p][1] = c

    tree[c][2] = p

cnt = 0
pre_order(1)
print(cnt)
for i in range(len(tree)):
    print(tree[i])