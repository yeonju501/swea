import sys
sys.stdin = open('5356_input.txt')

T = int(input())
for tc in range(1, T+1):
    print('#{}'.format(tc), end=' ')
    words = []
    for _ in range(5):
        words.append(input())
    i = 0
    while i < 15:
        for j in range(5):
            try:
                print(words[j][i], end='')
            except IndexError:
                continue
        i += 1
    print()



