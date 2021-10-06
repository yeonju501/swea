import sys
sys.stdin = open('11871_input.txt')

T = int(input())
for tc in range(1, T+1):
    arr = list(input())
    stack = []

    for i in range(len(arr)):
        if len(stack) == 0:
            stack.append(arr[i])
        else:
            if stack[len(stack)-1] == arr[i]:
                stack.pop()
            else:
                stack.append(arr[i])
    print('#{} {}'.format(tc, len(stack)))