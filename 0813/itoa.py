def itoa(x):
    arr = []
    while x :
        y = x % 10
        arr.append(y)
        x = x // 10
    arr.reverse()
    return arr

x = 123
print(x, type(x))
arr = itoa(x)
print(arr, type(arr))