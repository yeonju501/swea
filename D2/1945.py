T = int(input())
nums_list = []
for i in range(T):
    nums_list.append(int(input()))

for i in range(len(nums_list)):
    a = 0
    b = 0
    c = 0
    d = 0
    e = 0
    while nums_list[i] % 11 == 0:
        nums_list[i] //= 11
        e += 1
    while nums_list[i] % 7 == 0:
        nums_list[i] //= 7
        d += 1
    while nums_list[i] % 5 == 0:
        nums_list[i] //= 5
        c += 1
    while nums_list[i] % 3 == 0:
        nums_list[i] //= 3
        b += 1
    while nums_list[i] % 2 == 0:
        nums_list[i] //= 2
        a += 1
    print(f'#{i+1} {a} {b} {c} {d} {e}')