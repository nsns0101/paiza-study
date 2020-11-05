# 70점
# a = 프레임 수
# b = 핀 수
# c = 공을 던진 횟수
a, b, c = input().split(" ")
a, b, c = int(a), int(b), int(c)
pin_value = input().split(" ")
ball = []

#공을 던진 횟수 만큼 반복
count = 0
temp = []
strike_count = 0
for i in range(0, c):
    # G면 0으로 바꿔주기
    if(pin_value[i] == "G"):
        pin_value[i] = "0"
    
    temp.append( int(pin_value[i]) )
    # print(temp[i + strike_count])
    # 스트라이크의 경우 => i = 0이 아니고 10점이면서 앞에 G가 아닐때
    if( i != c - 1 and ( ( i == 0 and temp[i + strike_count] == b) or (i != 0 and temp[i + strike_count] == b and len(temp) % 2 != 0) )):
        temp.append('strike')
        strike_count+=1
    # print("temp => ", i, strike_count, temp)
    # print(temp)
print(temp)

score = 0
last_index = 0
if(len(temp) % 2 == 0):
    last_index = 2
else:
    last_index = 3

for i in range(0, len(temp) - last_index, 2):
    
    #스트라이크일 경우
    if(temp[i + 1] == "strike"):
        # print(temp[i + 1])
        # 그 다음도 스트라이크일 경우
        if(temp[i + 2] == b):
            score += temp[i] + temp[i + 2] + temp[i + 4]
        else:
            score += temp[i] + temp[i + 2] + temp[i + 3]
    #스페어일 경우
    elif(temp[i] + temp[i + 1]== b):
        # print("spare")
        score += temp[i] + temp[i + 1] + temp[i + 2]
    #일반
    else:
        # print("basic")
        score += temp[i] + temp[i+1]
    # print(score)
# print(score)


# print(temp[-3] + temp[-2])
if(last_index == 3):
    if(temp[-3] == "strike"):
        temp[-3] = b
    if(temp[-3] + temp[-2] == b):
        temp[-1] = temp[-1] * 2

for i in range(-last_index, 0, 1):
    # print(temp[i])
    score += temp[i]
print(score)
    


