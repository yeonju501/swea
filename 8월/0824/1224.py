import sys
sys.stdin = open('1224_input.txt')

for tc in range(1, 11):
    print('#{}'.format(tc), end=' ')
    N = int(input())
    s = input()
    S = ''
    stack = []
    for i in range(N):
        if s[i] == '(':
            stack.append(s[i])
        elif s[i] == '+':
            while stack :
                if stack[-1] == '(':
                    break
                S += stack.pop()
            stack.append(s[i])
        elif s[i] == '*':
            stack.append(s[i])
        elif s[i] == ')':
            while stack:
                if stack[-1] == '(':
                    stack.pop()
                    break
                S += stack.pop()
        else:
            S += s[i]
    for i in range(len(stack)):
        S += stack.pop()
    stack = []
    for i in range(len(S)):
        if S[i] == '+' or S[i] == '*':
            if len(stack) >= 2:
                b = int(stack.pop())
                a = int(stack.pop())
            if S[i] == '+':
                stack.append(a+b)
            else:
                stack.append(a*b)
        else:
            stack.append(S[i])
    print(stack.pop())







