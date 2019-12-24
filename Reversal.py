word = ""

word = input('What word would you like reversed today? >')

def reverse(word):
    str = ""
    for x in word:
        str = x + str
    return str

print(reverse(word))