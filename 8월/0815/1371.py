sentence = ''
result = [0] * 26
while True:
    try:
        sentence = input()
    except EOFError:
        break
    for letter in sentence:
        if letter == ' ':
            continue
        result[ord(letter)-97] += 1
m = max(result)
for i in range(len(result)):
    if result[i] == m:
        print(chr(i+97), end='')


    