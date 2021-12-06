import sys
sys.stdin = open('5658_input.txt')

for tc in range(1, int(input())+1):
    N, K = map(int, input().split())
    code = input()
    codes = [code]
    for i in range(1, N//4):
        codes.append(code[-1*i:] + code[:-1*i])
    s = []
    for i in range(N//4, N+1, N//4):
        for j in range(N//4):
            s.append(int(codes[j][i-N//4:i], 16))
    s = set(s)
    s = list(s)
    s.sort(reverse=True)
    print(f'#{tc} {s[K-1]}')