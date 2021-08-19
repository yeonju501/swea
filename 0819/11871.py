import sys
sys.stdin = open('11871_input.txt')

def check_str(s):
    stack = []
    top = -1
    for i in range(len(s)):
        if top >= 0 and s[i] == stack[top]:
            stack.pop()
            top -= 1
        else:
            stack.append(s[i])
            top += 1
    return len(stack)

T = int(input())
for tc in range(1, T+1):
    S = input()
    print('#{} {}'.format(tc, check_str(S)))