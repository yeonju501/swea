import sys
sys.stdin = open('1232_input.txt')


def postorder(s):
    if first_child[s]:
        postorder(first_child[s])
    if second_child[s]:
        postorder(second_child[s])
    if alpha[s]:
        b = int(stack.pop())
        a = int(stack.pop())
        if alpha[s] == '-':
            stack.append(a-b)
        elif alpha[s] == '*':
            stack.append(a*b)
        elif alpha[s] == '+':
            stack.append(a+b)
        else:
            stack.append(a//b)
    else:
        stack.append(num[s])


for tc in range(1, 11):
    print('#{}'.format(tc), end=' ')
    N = int(input())
    first_child = [0] * (N+1)
    second_child = [0] * (N+1)
    alpha = [''] * (N+1)
    num = [0] * (N+1)
    stack = []
    for i in range(N):
        arr = list(input().split())
        addr = int(arr[0])
        if arr[1].isdigit():
            num[addr] = int(arr[1])
        else:
            alpha[addr] = arr[1]
            first_child[addr] = int(arr[2])
            second_child[addr] = int(arr[3])
    postorder(1)
    print(stack.pop())


