import string


def findeMissingLetter(text):
    alphabets = string.ascii_lowercase
    start = alphabets.index(text[0])
    arr = []
    for letter in alphabets[start:]:
        if letter not in text:
            arr.append(letter)
        if letter == text[-1]:
            break
    return arr


print(findeMissingLetter("afl"))
