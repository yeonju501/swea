N = 20
q = [(1, 0)]

new_people = 1
last_people = 0
print(N, q)

while N > 0:
    num, cnt = q.pop(0)
    cnt += 1
    last_people = num

    N -= cnt
    new_people += 1

    q.append((num, cnt))
    q.append((new_people, 0))

    input()
    print(num, cnt, N, q)
print(last_people)