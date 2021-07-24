n = input()
arr = n.split(' ')
A = int(arr[0])
B = int(arr[1])
if A - B == 2 or B > A:
    print('B')
elif A > B or B - A == 2:
    print('A')