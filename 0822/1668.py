N = int(input())
t = [int(input()) for _ in range(N)]
cnt = 1
tall = t[0]
for i in range(1, len(t)):
    if t[i] > tall:
        cnt += 1
        tall = t[i]
print(cnt)

cnt2 = 1
tall2 = t[len(t)-1]

for i in range(len(t)-2, -1, -1):
    if t[i] > tall2:
        cnt2 += 1
        tall2 = t[i]
print(cnt2)
