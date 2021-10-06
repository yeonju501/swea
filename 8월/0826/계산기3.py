import sys
sys.stdin = open('1224_input.txt')

def priority(c):
    if c == '(': return 0 # 우선 낮은 것
    elif c == '+' or c == '-': return 1
    elif c == '*' or c == '/': return 2


def get_postfix(infix):
    stack = []
    postfix = []

    for i in range(len(infix)):
        if '0' <= infix[i] <= '9':
            postfix.append(infix[i])
        else:
            if infix[i] == '(':
                stack.append(infix[i])
            elif infix[i] == ')':
                while stack[-1] != '(':
                    postfix.append(stack.pop())
                stack.pop()
            else:
                if stack:
                    while priority(infix[i]) <= priority(stack[-1]):
                        postfix.append(stack.pop())
                        if not stack: break
                stack.append(infix[i])
    while stack:
        postfix.append(stack.pop())
    return ''.join(postfix)

def calc(postfix):
    stack = []
    for i in range(len(postfix)):
        if '0' <= postfix[i] <= '9':
            stack.append(int(postfix[i]))
        else:
            op2 = stack.pop()
            op1 = stack.pop()
            if postfix[i] == '+':
                stack.append(op1 + op2)
            else:
                stack.append(op1 * op2)
    return stack.pop()


T = 10
for tc in range(1, T+1):
    N = int(input())
    infix = input()
    postfix = get_postfix(infix)
    ans = calc(postfix)
    print('#{} {}'.format(tc, ans))