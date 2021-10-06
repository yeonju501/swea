import sys
sys.stdin = open('5432_input.txt')

T = int(input())
for tc in range(1, T+1):
    print('#{}'.format(tc), end=' ')
    s = input()
    stack = []
    laser = top = i = 0
    total = 0
    while i < len(s):
        if s[i] == '(':
            if s[i+1] == ')':
                for j in range(len(stack)):
                    stack[j] += 1
                i += 1
            else:
                stack.append(0)
            i += 1
        elif s[i] == ')':
            laser = stack.pop()
            total += laser + 1
            i += 1
    print(total)





