def my_strrev(text):
    arr = list(text) # str -> list
    for i in range(len(text)//2):
        arr[i], arr[len(arr)-1-i] = arr[len(arr)-1-i], arr[i]
    # list -> str
    string = ''.join(arr) # iterable => str
    return string

text = 'algorithm'
text1 = my_strrev(text)
print(text1)
arr = list(text) #문자열 리스트 변환 가능
arr.reverse()
text2 = ''.join(arr)
print(text2)

text3 = text[::-1]
print(text3)
