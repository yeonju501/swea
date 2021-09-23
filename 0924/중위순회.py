"""
8
1 W 2 3
2 F 4 5
3 R 6 7
4 O 8
5 T
6 A
7 E
8 S
"""

T = 1
for tc in range(1, T+1):
    N = int(input())
    first_child = [0] * (N+1)
    second_child = [0] * (N+1)
    alpha = [''] * (N+1)

    for i in range(N):
        temp = list(input().split())
        addr = int(temp[0])
        alpha[addr] = temp[1]
        if addr * 2 <= N: # 왼쪽자식
            first_child[addr] = int(temp[2])
            if addr * 2 + 1 <= N: #오른쪽 자식
                second_child[addr] = int(temp[3])
    print()