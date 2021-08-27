import sys
sys.stdin = open('중위순회_input.txt')

def inorder(s):
    if first_child[s]:
        inorder(first_child[s])
    print(alpha[s], end='')
    if second_child[s]:
        inorder(second_child[s])

for tc in range(1, 11):
    print('#{}'.format(tc), end=' ')
    N = int(input())
    first_child = [0] * (N+1)
    second_child = [0] * (N+1)
    alpha = [''] * (N+1)

    for i in range(N):
        temp = list(input().split())
        addr = int(temp[0])
        alpha[addr] = temp[1]
        if addr * 2 <= N:
            first_child[addr] = int(temp[2])
            if addr * 2 + 1 <= N:
                second_child[addr] = int(temp[3])

    inorder(1)
    print()