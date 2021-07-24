for i in range(5):
    for j in range(0, i):
        print('+', end = '')
    print('#', end = '')
    for x in range(4-i, 0, -1):
        print('+', end = '')
    print('')