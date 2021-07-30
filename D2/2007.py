T = int(input())
#문자열의 포문을 돌려 첫 글자와 같은 글자가 나올때 인덱스로 전체 인덱스를 나눠보자
words = []
for i in range(T):
    words.append(input())
for i in range(len(words)):
    for j in range(len(words[i])):
        if words[i][:j+1] == words[i][j+1:(j+1)*2]:
            print(f'#{i + 1} {j+1}')
            break
