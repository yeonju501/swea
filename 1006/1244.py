import sys
sys.stdin = open('1244_input.txt')

T = int(input())
for tc in range(1, T+1):
    num, c = input().split()
    c = int(c)
    num = list(num)
    num_s = sorted(num, reverse=True)
    while c != 0:
        if num == num_s:
            num[-1], num[-2] = num[-2], num[-1]
            c -= 1
        else:
            for i in range(len(num)):
                if num[i] != num_s[i]:
                    idx = num.index(num_s[i])
                    num[i], num[idx] = num[idx], num[i]
                    c -= 1
                    break

    print(num)

