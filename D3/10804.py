for T in range(int(input())):
    word = input() 
    # 1 q -1 p 5 p -5 q
    # 1 b -1 d 2 d -2 b
    new = ''
    for letter in word:
        if letter == 'p':
            new = 'q' + new
        elif letter == 'q':
            new = 'p'+ new
        elif letter == 'b':
            new = 'd' + new
        else:
            new = 'b' + new
    print(f'#{T+1} {new}')
    

