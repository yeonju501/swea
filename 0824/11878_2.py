import sys
sys.stdin = open('11878_input.txt')

T = int(input())
for tc in range(1, T+1):
    print('#{}'.format(tc), end=' ')
    s = input().split()
    stack = [s[0], s[1]]
    for i in range(2, len(s)):
        if s[i] == '+' or s[i] == '*' or s[i] == '-' or s[i] == '/':
            if len(stack) >= 2:
                b = int(stack.pop())
                a = int(stack.pop())
                if s[i] == '+':
                    stack.append(a + b)
                elif s[i] == '*':
                    stack.append(a * b)
                elif s[i] == '-':
                    stack.append(a - b)
                elif s[i] == '/':
                    stack.append(a // b)
            else:
                print('error')
                break
        elif s[i] == '.':
            if len(stack) == 1:
                print(stack.pop())
                break
            else:
                print('error')
                break
        else:
            stack.append(s[i])