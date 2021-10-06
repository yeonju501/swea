import sys
sys.stdin = open('11866_input.txt')

def cnt_word(s1, s2):
    m = 0
    l = len(s1)
    arr = [0] * l
    for i in range(len(s2)):
        for j in range(l):
            if s1[j] == s2[i]:
                arr[j] += 1
    for i in range(l):
        if arr[i] > m:
            m = arr[i]
    return m

T = int(input())
for tc in range(1, T+1):
    print('#{}'.format(tc), end=' ')
    str1 = input()
    str2 = input()
    print(cnt_word(str1, str2))
