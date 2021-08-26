import sys
sys.stdin = open('11881_input.txt')

def game(left, right):
    if left == right:
        return left
    else:
        result1 = game(left, (left + right)//2)
        result2 = game((left + right)//2 + 1, right)
    # 가위바위보
    if arr[result1] == arr[result2]:
        return result1
    else:
        if arr[result1] == 1 and arr[result2] == 2:
            return result2
        elif arr[result1] == 1 and arr[result2] == 3:
            return result1
        elif arr[result1] == 2 and arr[result2] == 1:
            return result1
        elif arr[result1] == 2 and arr[result2] == 3:
            return result2
        elif arr[result1] == 3 and arr[result2] == 1:
            return result2
        elif arr[result1] == 3 and arr[result2] == 2:
            return result1


T = int(input())
for tc in range(1, T+1):
    N = int(input())
    arr = [0] + list(map(int, input().split()))
    print('#{} {}'.format(tc, game(1, N)))