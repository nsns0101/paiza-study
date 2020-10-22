# 80% 1h 15m
number = int(input())

player = list(input().split(" "))
# print(number)
# print(player)

arr = list(set(player))
count = []

#중복 제거한 플레이어를 제거한 배열길이 만큼 count배열을 만들어줌
for i in range(0, len(list(set(player)))):
    count.append(0)
print(count)

# 갯수찾기
for i in range(0, len(arr)):
    for j in range(0, number):
        if(arr[i] == player[j]):
            count[i] +=1
# print(arr)
# print((count))

result = []
for i in range(0, len(count)):
    if(count[i] == max(count)):
        result.append(arr[i])

result.sort()   #오름차순
print(' '.join(result))

