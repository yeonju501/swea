q = []
j = 1
m = 0
while True:
    q.append([j, 1])
    i = q.pop(0)
    m += 1
    if m == 20:
        print(i[0])
        break
    i[1] += 1
    q.append(i)
    j += 1