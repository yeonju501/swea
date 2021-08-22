N, M, K = map(int, input().split())
T = 0
while True:
    if K == 0:
        while N > 1 and M > 0:
            N -= 2
            M -= 1
            T += 1
        break
    if M * 2 <= N:
        N -= 1
        K -= 1
    else:
        M -= 1
        K -= 1
print(T)