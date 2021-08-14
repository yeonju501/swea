def brute_force(t, p):
    N = len(t)
    M = len(p)

    for i in range(N-M+1):
        flag = 1
        for j in range(M):
            if t[i+j] != p[j]:
                flag = 0
                break
        if flag:
            return i
    return -1


t = "a pattern matching algorithm"
p = "rithm"
print(t.find(p))
print(brute_force(t, p))