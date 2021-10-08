import sys
sys.stdin = open('4366_input.txt')

def check():
    for i in range(0, len(t), 2):
        for j in range(len(b)):
            te1 = int(''.join(t[i]), 3)
            te2 = int(''.join(t[i+1]), 3)
            bi = int(''.join(b[j]), 2)
            if te1 == bi or te2 == bi:
                return int(''.join(b[j]), 2)


for tc in range(1, int(input())+1):
    binary = list(input())
    b = []
    ternary = list(input())
    t = []
    for i in range(len(binary)):
        new = binary.copy()
        if binary[i] == '1':
            new[i] = '0'
        else:
            new[i] = '1'
        b.append(new)

    for i in range(len(ternary)):
        new = ternary.copy()
        new2 = ternary.copy()
        if ternary[i] == '1':
            new[i] = '0'
            new2[i] = '2'
        elif ternary[i] == '0':
            new[i] = '1'
            new2[i] = '2'
        else:
            new[i] = '0'
            new2[i] = '1'
        t.append(new)
        t.append(new2)

    print('#{} {}'.format(tc, check()))





