import sys
sys.stdin = open('11878_input.txt')

def forth():
    stack = []
    for i in range(len(arr)):
        if arr[i] == '+' or arr[i] == '-' or arr[i] == '/' or arr[i] == '*':
            if len(stack) >= 2:
                op2 = int(stack.pop())
                op1 = int(stack.pop())
                if arr[i] == '+':
                    stack.append(op1 + op2)
                elif arr[i] == '-':
                    stack.append(op1 - op2)
                elif arr[i] == '*':
                    stack.append(op1 * op2)
                elif arr[i] == '/':
                    stack.append(op1 // op2)
            else:
                return 'error'
        elif arr[i] != '.': # isdigit()
            stack.append(arr[i])
        elif arr[i] == '.':
            if len(stack) == 1:
                return stack.pop()
            else:
                return 'error'
T = int(input())
for tc in range(1, T+1):
    arr = list(input().split())
    print('#{} {}'.format(tc, forth()))