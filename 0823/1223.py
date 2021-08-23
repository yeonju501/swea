import sys
sys.stdin = open('1223_input.txt')

for tc in range(1, 11):
    print('#{}'.format(tc), end=' ')
    N = int(input())
    s = input()
    num = ''
    num += s[0]
    stack = []
    stack.append(s[1])
    top = 0
    for i in range(2, N):
        if s[i] == '+':
            while len(stack) > 0:
                if stack[top] == '+':
                    num += stack.pop()
                    top -= 1
                    break
                op = stack.pop()
                top -= 1
                num += op
            stack.append(s[i])
            top += 1
        elif s[i] == '*':
            stack.append(s[i])
            top += 1
        else:
             num += s[i]
    else:
        while top != -1:
            num += stack.pop()
            top -= 1
    stack = []
    for i in range(len(num)):
        if num[i] == '+' or num[i] == '*':
            b = int(stack.pop())
            a = int(stack.pop())
            if num[i] == '+':
                stack.append(a + b)
            else:
                stack.append(a * b)
        else:
            stack.append(num[i])
    else:
        print(stack.pop())



