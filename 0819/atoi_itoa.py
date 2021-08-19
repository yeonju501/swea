def itoa(x):
    arr = []
    while x:
        y = x % 10 # 나머지
        x = x // 10 # 몫
        arr.append(y)
    arr.reverse()
    return arr

def swap(arr, i, j):
    arr[i], arr[j] = arr[j], arr[i]

def atoi(arr):
    v = 0
    for i in range(len(arr)):
        v = (v * 10) + arr[i]
        # 2진수는 10을 2로 바꿔서
    return v
x1 = 123
print(x1, type(x1))
x2 = itoa(x1)
print(x2, type(x2))
swap(x2, 0, 1)
print(x2, type(x2))
x3 = atoi(x2)
print(x3)

