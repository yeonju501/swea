import sys
sys.stdin = open('11870_input.txt')

def check(S):
    stack = []
    top = 0
    ob = {'{': 0, '(': 1}
    cb = {'}': 0, ')': 1}
    for i in range(len(S)):
        if S[i] in ob.keys():
            stack.append(S[i])
            top += 1
        elif S[i] in cb.keys():
            try:
                j = stack.pop()
            except IndexError:
                return 0
            top -= 1
            if cb[S[i]] != ob[j]:
                return 0
    if top:
        return 0
    else:
        return 1

T = int(input())
for tc in range(1, T+1):
    s = input()
    print('#{} {}'.format(tc, check(s)))


