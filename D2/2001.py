T = int(input())
for t in range(T):
    ns = []
    N, M = map(int, input().split())
    for z in range(N):
        ns.append(list(map(int,input().split())))
        max = 0
        for i in range(0, len(ns)-M+1):
            for j in range(0, len(ns[i])-M+1):
                num_flies = 0
                for x in range(M):
                    for y in range(M):
                        num_flies += ns[i+x][j+y]  
                if num_flies > max:
                    max = num_flies
    print(f'#{t+1} {max}')
