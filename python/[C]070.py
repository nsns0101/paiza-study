#53m 100% 
number = int(input())

card = []

# number길이 만큼 입력하기
for i in range(0, number):
    card.append(input())

# print(card)
temp = []
count = []
# arr = []
for i in range(0, number):
    # 중복값 제거하고 값을 넣음 7777이면 '7', '7', '7' ,'7'
    temp.append(list(set(card[i])))     
    # count길이 추가
    count.append(0)

    arr = list(card[i])
    # print(arr)
    for j in range(0, 4):
        for k in range(0, 4):
            if(j == k):
                continue
            if(arr[j] == arr[k]):
                # print(arr[j], arr[k])
                count[i] +=1
                break
# print(arr)
# print(count)
    
# print(temp)

result = []
for i in range(0, len(temp)):
    # 포카드
    if(len(temp[i]) == 1):
        result.append("Four Card")
    # 트리플
    elif(len(temp[i]) == 2 and count[i] == 3):
        result.append("Three Card")
    # 투페어
    elif(len(temp[i]) == 2 and count[i] == 4):
        result.append("Two Pair")
    # 원페어
    elif(len(temp[i]) == 3):
        result.append("One Pair")
    # 노페어
    else:
        result.append("No Pair")

        
for i in range(0, len(result)):
    print(result[i])



