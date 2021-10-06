for _ in range(10):
    tc, N = map(int, input().split())
    road = list(map(int, input().split()))

    adj_list = [[] for _ in range(100)]
    for i in range(N):
        # 인접리스트
        adj_list[road[2*i]].append(road[2*1+1])

    visited = [0] * 100
    ans = 0

    stack = [0]

    while stack:
        curr = stack.pop()

        if curr == 99 :
            ans = 1
            break
        # 방문하지 않았으면
        # 방문을 했으면
        if visited[curr]: continue
        visited[curr] = 1

        for w in adj_list[curr]:
            if not visited[w]:
                stack.append(w)
    print('#{} {}'.format(tc, ans))