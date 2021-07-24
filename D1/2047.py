n = input()
for letter in n:
    if letter.isalpha():
        print(f'{letter.upper()}', end = '')
    else:
        print(letter, end = '')