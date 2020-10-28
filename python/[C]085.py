t = input().split(" ")
t = list(map(int, t))
# print(t)

word = list(input())
# print(word)

for i in range(0, len(t)):
    # [ ["a", 1], ["b", 3] ... ]
    t[i] = [ t[i], chr(97 + i)]

# print(t)
result = []
for i in range(0, len(word)):
    for j in range(0, len(t)):
        
        if(t[j][0] == 0):
            continue 

        elif(word[i] == t[j][1]):
            result.append(word[i])
            t[j][0]-=1

print("".join(result))


