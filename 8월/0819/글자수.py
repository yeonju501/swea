import sys
sys.stdin = open('11866_input.txt')

T = int(input())
for tc in range(1, T+1):
    str1 = input()
    str2 = input()
    asc = [0] * 128
    alph = [] # str1 중복제거된 배열
    for i in range(len(str1)):
        asc[ord(str1[i])] = 1
    for i in range(len(asc)):
        if asc[i]:
            alph.append(chr(i))

    for i in range(len(str2)):
        for j in range(len(alph)):
            if str2[i] == alph[i]:
                asc[ord[str2[i]]] += 1

    max = 0
    for i in range(len(asc)):
        if max < asc[i]:
            max = asc[i]

    print('#{} {}'.format(tc, max))