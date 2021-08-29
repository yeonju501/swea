import sys
sys.stdin = open('1248_input.txt')

def postorder(s, c):
    if first_child[s]:
        postorder(first_child[s], c)
    if s == c:
        visited.append(s)
    elif c in visited:
        visited.append(s)
    if second_child[s]:
        postorder(second_child[s], c)

T = int(input())
for tc in range(1, T+1):
    V, E, c1, c2 = map(int, input().split())
    edges = list(map(int, input().split()))
    first_child = [0] * (V+1)
    second_child = [0] * (V+1)
    for i in range(E):
        if not first_child[edges[2 * i]]:
            first_child[edges[2 * i]] = edges[2 * i + 1]
        else:
            second_child[edges[2 * i]] = edges[2 * i + 1]
    visited = []
    postorder(1, c1)
    postorder(1, c2)
    print(visited)

