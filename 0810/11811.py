import sys
sys.stdin = open('11811_input.txt')
T = int(input())
for tc in range(1, T+1):
    print('#{}'.format(tc), end=' ')
    N = int(input())
    a = input()
    A = [] #원본 배열
    B = [0] * N #정렬 배열
    C = [0] * 10 # 카운트 배열
    for num in range(len(a)):
        C[int(a[-1])] += 1
        A.append(int(a[-1]))
        a = a[0:-1]
    max = C[0]
    Idx = 0
    for i in range(len(C)):
        if C[i] >= max and i > Idx:
            max = C[i]
            Idx = i
    print(Idx, max)
    for i in range(1, len(C)):
        C[i] += C[i-1]
    for i in range(len(A)-1, -1, -1):
        B[C[A[i]]-1] = A[i] # 4~0
        C[A[i]-1] -= 1


