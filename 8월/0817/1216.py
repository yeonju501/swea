import sys
sys.stdin = open('1216_input.txt')

for tc in range(1, 11):
    print('#{}'.format(tc), end=' ')
    T = input()
    arr = [input() for _ in range(100)]
    start = 0
    end = 99
    max = 0
    for j in range(100):
        for x in range(2, 98):
            for y in range(100-x+1):
                for i in range(x//2+1):
                    if arr[j][y+i] != arr[j][y+x-i-1]:
                        break
                else:
                    if max < x:
                        max = x
                for i in range(x//2+1):
                    if arr[y+i][j] != arr[y+x-i-1][j]:
                        break
                else:
                    if max < x:
                        max = x
    print(max)










