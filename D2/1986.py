T = int(input())

for n in range(T):
    num = int(input())
    hap = 0
    for i in range(1, num + 1):
        if i % 2 :
            hap += i
        else:
            hap -= i
    print(f'#{n+1} {hap}')