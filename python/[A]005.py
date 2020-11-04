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
for i in range(0, c):
    
    if( len(temp) % 2 == 0):
        ball.append(temp)
        temp.clear()
        print("temp 초기화")

    # G면 0으로 바꿔주기
    if(pin_value[i] == "G"):
        pin_value[i] = "0"
    
    temp.append( int(pin_value[i]) )
    print("temp =>", temp)
    # 스트라이크의 경우 => i = 0이 아니고 10점이면서 앞에 G가 아닐때
    if(len(temp) != 1 and temp[i] == 10 and temp[i-1] != 0):
        temp.append(0)
    # 스페어, 일반 점수일 경우
    # elif(i != c-3 and temp[i] != 10):
        # temp.append(temp)
    # elif(i == c-3)
    
    print("ball => ", i, ball)
print(ball)
