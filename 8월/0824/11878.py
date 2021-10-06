import sys
sys.stdin = open('11878_input.txt')

T = int(input())
for tc in range(1, T+1):
    print('#{}'.format(tc), end=' ')
    s = input().split()
    stack = []
    for i in range(len(s)):
        if s[i] == '+' or s[i] == '*' or s[i] == '/' or s[i] == '-':
            if len(stack) >= 2:
                b = int(stack.pop())
                a = int(stack.pop())
                if s[i] == '+':
                    stack.append(a+b)
                elif s[i] == '*':
                    stack.append(a*b)
                elif s[i] == '/':
                    stack.append(a//b)
                else:
                    stack.append(a-b)
            else:
                ans = 'error'
                break
        elif s[i] == '.':
            if len(stack) == 1:
                ans = stack.pop()
                break
            else:
                ans = 'error'
                break
        else:
            stack.append(s[i])
    print(ans)
