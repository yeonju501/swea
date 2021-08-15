letters = input()
word = ['ABC', 'DEF', 'GHI', 'JKL', 'MNO', 'PQRS', 'TUV', 'WXYZ']
hap = 0
for i in range(len(word)):
    for j in range(len(letters)):
        if letters[j] in word[i]:
            hap += i + 3
print(hap)
