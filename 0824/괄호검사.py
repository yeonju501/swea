import sys
sys.stdin = open('11870_input.txt')

def solve(arr):
    global flag
    stack = []
    for i in range(len(arr)):
        # 여는 괄호 => push
        if arr[i] == '(' or arr[i] == '{':
            stack.append(arr[i])
        # 닫는 괄호 => isEmpty, pop, 짝검사
        elif arr[i] == ')' or arr[i] == '}':
            if len(stack) == 0: #isEmpty
                flag = 0
                return 0
            else:
                temp = stack.pop()

            if arr[i] == ')':
                if temp != '(':
                    flag = 0
                    return 0
            elif arr[i] == '}':
                if temp != '{':
                    flag = 0
                    return 0
    if len(stack) != 0:
        flag = 0
        return 0
    return 1

    # isEmpty


T = int(input())
for tc in range(1, T+1):
    arr = list(input())
    flag = 1 # 참이라고 가정
    solve(arr)
    print('#{} {}'.format(tc, flag))