for tc in range(1, int(input())+1):
    N = int(input())
    num = list(input())
    dic = { # 이진수를 저장하는 딕셔너리
        '1': '0001',
        '2': '0010',
        '3': '0011',
        '4': '0100',
        '5': '0101',
        '6': '0110',
        '7': '0111',
        '8': '1000',
        '9': '1001',
        'A': '1010',
        'B': '1011',
        'C': '1100',
        'D': '1101',
        'E': '1110',
        'F': '1111'
    }
    arr = [0] * 10
    num_str = ''
    for i in range(len(num)): # 16진수를 2진수로 바꿔서 num_str에 추가함
        num_str += dic[num[i]]
    cnt = 0
    for i in range(len(num_str)): # 포문을 돌려 1값이 나올때마다 cnt 증가 0이 나올 시 arr에 저장
        if num_str[i] == '1':
            cnt += 1
        elif num_str[i] == '0':
            arr[cnt] += 1
            cnt = 0
    else:
        arr[cnt] += 1
    print('#{}'.format(tc), end=' ')
    for i in range(1, 10):
        print(arr[i], end=' ')
    print()

