import sys
sys.stdin = open('1240_input.txt')

def get_pw():
    for i in range(h-1, -1, -1):
        for j in range(w-1, -1, -1):
            if arr[i][j] == '1':
                return i, j-55

def get_pw_num():
    for i in range(8):
        for j in range(10):
            if pw_s[i] == nums[j]:
                pw_num.append(j)

T = int(input())
for tc in range(1, T+1):
    h, w = map(int, input().split())
    arr = [input() for _ in range(h)]
    nums = ['0001101', '0011001', '0010011', '0111101', '0100011', '0110001', '0101111', '0111011', '0110111', '0001011']
    i, j = get_pw()
    pw = arr[i][j:j+56]
    pw_s = []
    pw_num = []
    for i in range(0, 56, 7):
        pw_s.append(pw[i:i+7])
    get_pw_num()
    code = 0
    for i in range(8):
        if i % 2:
            code += pw_num[i]
        elif i % 2 == 0:
            code += pw_num[i]*3
    if code % 10:
        print('#{} {}'.format(tc, 0))
    else:
        print('#{} {}'.format(tc, sum(pw_num)))


