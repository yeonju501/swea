# 1 / 1 1 /  1 1+1 1 / 1 1+2 1+2 1 / 1 1+3 3+3 1+3 1 / 1 1+4 4+6 4+6 1+4 1 
# 1 1+5 5+10 10+10 5+10 1+5 1 / 1 1+6 6+15 15+20 15+20 6+15 1+6 1
T = int(input())
su = []
for x in range(T):
    su.append(int(input()))
for y in range(len(su)):
        arr = []
        print(f'#{y+1}')
        for i in range(0, su[y]):
            new = []
            arr.append(new)
            for j in range(0, i+1):
                if i == j or j == 0 :
                    new.append(1)    
                else:
                    new.append(arr[i-1][j-1] + arr[i-1][j])
                print(arr[i][j], end = ' ')
            print('')
