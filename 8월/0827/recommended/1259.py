import sys
sys.stdin = open('1259_input.txt')

T = int(input())
for tc in range(1, T+1):
    print('#{}'.format(tc), end=' ')
    N = int(input())
    arr = list(map(int, input().split()))
    s = []
    ans = []
    while len(arr) != 0:
        p2 = arr.pop() # 5
        p1 = arr.pop() # 4
        if p1 in arr:
            idx = arr.index(p1)
            if idx % 2:
                a1 = arr.pop(idx-1)
                a2 = arr.pop(idx-1)
                ans.extend([str(a1), str(a2), str(p1), str(p2)])
        else:
            s.append(str(p1))
            s.append(str(p2))
    ans = s + ans
    for i in ans:
        print(i, end=' ')
    print()














