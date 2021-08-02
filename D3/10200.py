for x in range(int(input())):
    N, P, T = map(int, input().split())
    max = 0
    min = 0
    if P <= T:
        if P + T > N:
           min = T + P - N
        else:
           min = 0  
        max = P
    else:
        if P + T > N:
            min = T + P - N
        else:
            min = 0
        max = T
    print(f'#{x+1} {max} {min}')

