word = list(input())
result = []
for i in range(0, len(word)):
    if(word[i] == "a" or word[i] == "e" or word[i] == "i" or word[i] == "o" or word[i] == "u"
        or word[i] == "A" or word[i] == "E" or word[i] == "I" or word[i] == "O" or word[i] == "U"):
        continue
    else:
        result.append(word[i])

print( "".join(result) )