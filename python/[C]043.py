# 80% 1h 15m
number = int(input())

player = list(input().split(" "))
# print(number)
# print(player)

arr = []
temp = 0
count = [0]
# temp_count = 0
for i in range(0, number):
    temp = 0

    # 첫 생성시
    if(len(arr) == 0):
        arr.append(player[i])
        continue    

    for j in range(0, len(arr)):
        # player가 arr에 없으면 없다는 카운트 ++
        if(player[i] != arr[j]):
            # print("없는 숫자")
            temp += 1
        else:
            # print("이미 있는 숫자")
            break
        # print(temp)


    if(temp == len(arr)):
        # print(temp, len(arr))
        arr.append(player[i])
        count.append(0)
# print(arr)      
# print(count)

good = 0

for i in range(0, len(arr)):
    for j in range(0, number):
        if(arr[i] == player[j]):
            count[i] +=1
# print(max(count))

result = []
for i in range(0, len(arr)):
    if(count[i] == max(count)):
        result.append(arr[i])

result.sort()
# result.reverse()
print(' '.join(result))

