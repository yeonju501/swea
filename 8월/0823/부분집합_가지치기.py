def powerset(n, k, cur_sum): # n : 원소의 갯수, k : 현재 depth
    global cnt
    if cur_sum > 10:
        return
    cnt += 1
    if n == k:
        if cur_sum == 10:
            for i in range(n):
                if bit[i]:
                    print(arr[i], end=' ')
            print()
    else:
        bit[k] = 1
        powerset(n, k + 1, cur_sum + arr[k])
        bit[k] = 0
        powerset(n, k + 1, cur_sum)

arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
N = len(arr)
bit = [0] * N
cnt = 0
powerset(N, 0, 0)
print(cnt)