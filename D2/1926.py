num = int(input())
# 빈 리스트에 숫자를 str으로 담아서 인덱스마다 검사한다.
# 숫자 count 3 6 9 해서 2개면 -- 3개면 ---
num_str = []
for i in range(1, num + 1):
    num_str.append(str(i))
for i in range(len(num_str)):
    num_cnt = 0
    num_cnt += num_str[i].count('3')
    num_cnt += num_str[i].count('6')
    num_cnt += num_str[i].count('9')
    if num_cnt != 0:
        num_str[i] = '-' * num_cnt
print(' '.join(num_str))
